import numpy as np
from skimage.filters import gabor_kernel
import cv2
import dlib
import os

class KernelParams:
    """
    A simple class to represent the parameters of a given Gabor kernel.
    """

    #---------------------------------------------
    def __init__(self, wavelength, orientation):
        """
        Class constructor. Define the parameters of a Gabor kernel.

        Parameters
        ----------
        wavelength: float
            Wavelength (in pixels) of a Gabor kernel.
        orientation: float
            Orientations (in radians) of a Gabor kernel.
        """

        self.wavelength = wavelength
        """Wavelength (in pixels) of a Gabor kernel."""

        self.orientation = orientation
        """Orientation (in radians) of a Gabor kernel."""

    #---------------------------------------------
    def __hash__(self):
        """
        Generates a hash value for this object instance.

        Returns
        ----------
        hash: int
            Hash value of this object.
        """
        return hash((self.wavelength, self.orientation))

    #---------------------------------------------
    def __eq__(self, other):
        """
        Verifies if this object instance is equal to another.

        This method is the implementation of the == operator.

        Parameters
        ----------
        other: KernelParams
            Other instance to compare with this one.

        Returns
        ----------
        eq: bool
            True if this and the other instances have the same parameters, or
            False otherwise.
        """
        return (self.wavelength, self.orientation) == \
               (other.wavelength, other.orientation)

    #---------------------------------------------
    def __ne__(self, other):
        """
        Verifies if this object instance is different than another.

        This method is the implementation of the != operator.

        Parameters
        ----------
        other: KernelParams
            Other instance to compare with this one.

        Returns
        ----------
        neq: bool
            True if this and the other instances have different parameters, or
            False otherwise.
        """
        return not(self == other)
class GaborBank:
    """
    Represents a bank of gabor kernels.
    """

    #---------------------------------------------
    def __init__(self, w = [4, 7, 10, 13],
                       o = [i for i in np.arange(0, np.pi, np.pi / 8)]):
        """
        Class constructor. Create a bank of Gabor kernels with a predefined set
        of wavelengths and orientations.

        The bank is composed of one kernel for each combination of wavelength x
        orientation. For the rationale regarding the choice of parameters, refer
        to the PhD thesis of the author of this code.
        """

        self._wavelengths = w
        """
        List of wavelengths (in pixels) used to create the bank of Gabor
        kernels.
        """

        self._orientations = o
        """
        List of orientations (in radians) used to create the bank of Gabor
        kernels.
        """

        self._kernels = {}
        """Dictionary holding the Gabor kernels in the bank."""

        # Create one kernel for each combination of wavelength x orientation
        for wavelength in self._wavelengths:
            for orientation in self._orientations:
                # Convert wavelength to spatial frequency (scikit-image's
                # interface expects spatial frequency, even though the original
                # equation uses wavelengths - see https://en.wikipedia.org/wiki/
                # Gabor_filter/)
                frequency = 1 / wavelength

                # Create and save the kernel
                kernel = gabor_kernel(frequency, orientation)
                par = KernelParams(wavelength, orientation)
                self._kernels[par] = kernel

    #---------------------------------------------
    def filter(self, image):
        """
        Filter the given image with the Gabor kernels in this bank.

        Parameters
        ----------
        image: numpy.array
            Image to be filtered.

        Returns
        -------
        responses: numpy.array
            List of the responses of the filtering with the Gabor kernels. The
            responses are the magnitude of both the real and imaginary parts of
            the convolution with each kernel, hence this list dimensions are the
            same of the image, plus another dimension for the 32 responses (one
            for each kernel in the bank, since there are 4 wavelengths and 8
            orientations).
        """

        image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        responses = []
        for wavelength in self._wavelengths:
            for orientation in self._orientations:

                # Get the kernel
                frequency = 1 / wavelength
                par = KernelParams(wavelength, orientation)
                kernel = self._kernels[par]

                # Filter with both real and imaginary parts
                real = cv2.filter2D(image, cv2.CV_32F, kernel.real)
                imag = cv2.filter2D(image, cv2.CV_32F, kernel.imag)

                # The response is the magnitude of the real and imaginary
                # responses to the filters, normalized to [-1, 1]
                mag = cv2.magnitude(real, imag)
                cv2.normalize(mag, mag, -1, 1, cv2.NORM_MINMAX)

                responses.append(mag)

        return np.array(responses)
class FaceData:
    """
    Represents the data of a face detected on an image.
    """

    _jawLine = [i for i in range(17)]
    """
    Indexes of the landmarks at the jaw line.
    """

    _rightEyebrow = [i for i in range(17,22)]
    """
    Indexes of the landmarks at the right eyebrow.
    """

    _leftEyebrow = [i for i in range(22,27)]
    """
    Indexes of the landmarks at the left eyebrow.
    """

    _noseBridge = [i for i in range(27,31)]
    """
    Indexes of the landmarks at the nose bridge.
    """

    _lowerNose = [i for i in range(30,36)]
    """
    Indexes of the landmarks at the lower nose.
    """

    _rightEye = [i for i in range(36,42)]
    """
    Indexes of the landmarks at the right eye.
    """

    _leftEye = [i for i in range(42,48)]
    """
    Indexes of the landmarks at the left eye.
    """

    _outerLip = [i for i in range(48,60)]
    """
    Indexes of the landmarks at the outer lip.
    """

    _innerLip = [i for i in range(60,68)]
    """
    Indexes of the landmarks at the inner lip.
    """

    #---------------------------------------------
    def __init__(self, region = (0, 0, 0, 0),
                 landmarks = [0 for i in range(136)]):
        """
        Class constructor.

        Parameters
        ----------
        region: tuple
            Left, top, right and bottom coordinates of the region where the face
            is located in the image used for detection. The default is all 0's.
        landmarks: list
            List of x, y coordinates of the 68 facial landmarks in the image
            used for detection. The default is all 0's.
        """

        self.region = region
        """
        Region where the face is found in the image used for detection. This is
        a tuple of int values describing the region in terms of the top-left and
        bottom-right coordinates where the face is located.
        """

        self.landmarks = landmarks
        """
        Coordinates of the landmarks on the image. This is a numpy array of
        pair of values describing the x and y positions of each of the 68 facial
        landmarks.
        """

    #---------------------------------------------
    def copy(self):
        """
        Deep copies the data of the face.

        Deep copying means that no mutable attribute (like tuples or lists) in
        the new copy will be shared with this instance. In that way, the two
        copies can be changed independently.

        Returns
        -------
        ret: FaceData
            New instance of the FaceDate class deep copied from this instance.
        """
        return FaceData(self.region, self.landmarks.copy())

    #---------------------------------------------
    def isEmpty(self):
        """
        Check if the FaceData object is empty.

        An empty FaceData object have region and landmarks with all 0's.

        Returns
        ------
        response: bool
            Indication on whether this object is empty.
        """
        return all(v == 0 for v in self.region) or \
               all(vx == 0 and vy == 0 for vx, vy in self.landmarks)

    #---------------------------------------------
    def crop(self, image):
        """
        Crops the given image according to this instance's region and landmarks.

        This function creates a subregion of the original image according to the
        face region coordinates, and also a new instance of FaceDate object with
        the region and landmarks adjusted to the cropped image.

        Parameters
        ----------
        image: numpy.array
            Image that contains the face.

        Returns
        -------
        croppedImage: numpy.array
            Subregion in the original image that contains only the face. This
            image is shared with the original image (i.e. its data is not
            copied, and changes to either the original image or this subimage
            will affect both instances).

        croppedFace: FaceData
            New instance of FaceData with the face region and landmarks adjusted
            to the croppedImage.
        """
        left = self.region[0]
        top = self.region[1]
        right = self.region[2]
        bottom = self.region[3]

        croppedImage = image[top:bottom+1, left:right+1]

        croppedFace = self.copy()
        croppedFace.region = (0, 0, right - left, bottom - top)
        croppedFace.landmarks = [[p[0]-left, p[1]-top] for p in self.landmarks]

        return croppedImage, croppedFace

    #---------------------------------------------
    def draw(self, image, drawRegion = None, drawFaceModel = None):
        """
        Draws the face data over the given image.

        This method draws the facial landmarks (in red) to the image. It can
        also draw the region where the face was detected (in blue) and the face
        model used by dlib to do the prediction (i.e., the connections between
        the landmarks, in magenta). This drawing is useful for visual inspection
        of the data - and it is fun! :)

        Parameters
        ------
        image: numpy.array
            Image data where to draw the face data.
        drawRegion: bool
            Optional value indicating if the region area should also be drawn.
            The default is True.
        drawFaceModel: bool
            Optional value indicating if the face model should also be drawn.
            The default is True.

        Returns
        ------
        drawnImage: numpy.array
            Image data with the original image received plus the face data
            drawn. If this instance of Face is empty (i.e. it has no region
            and no landmarks), the original image is simply returned with
            nothing drawn on it.
        """
        if self.isEmpty():
            raise RuntimeError('Can not draw the contents of an empty '
                               'FaceData object')

        # Check default arguments
        if drawRegion is None:
            drawRegion = True
        if drawFaceModel is None:
            drawFaceModel = True

        # Draw the region if requested
        if drawRegion:
            cv2.rectangle(image, (self.region[0], self.region[1]),
                                 (self.region[2], self.region[3]),
                                 (0, 0, 255), 2)

        # Draw the positions of landmarks
        color = (0, 255, 255)
        for i in range(68):
            cv2.circle(image, tuple(self.landmarks[i]), 1, color, 2)

        # Draw the face model if requested
        if drawFaceModel:
            c = (0, 255, 255)
            p = np.array(self.landmarks)

            cv2.polylines(image, [p[FaceData._jawLine]], False, c, 2)
            cv2.polylines(image, [p[FaceData._leftEyebrow]], False, c, 2)
            cv2.polylines(image, [p[FaceData._rightEyebrow]], False, c, 2)
            cv2.polylines(image, [p[FaceData._noseBridge]], False, c, 2)
            cv2.polylines(image, [p[FaceData._lowerNose]], True, c, 2)
            cv2.polylines(image, [p[FaceData._leftEye]], True, c, 2)
            cv2.polylines(image, [p[FaceData._rightEye]], True, c, 2)
            cv2.polylines(image, [p[FaceData._outerLip]], True, c, 2)
            cv2.polylines(image, [p[FaceData._innerLip]], True, c, 2)

        return image
class GaborData:
    """
    Represents the responses of the Gabor bank to the facial landmarks.
    """

    #---------------------------------------------
    def __init__(self, features = [0.0 for i in range(2176)]):
        """
        Class constructor.

        Parameters
        ----------
        features: list
            Responses of the filtering with the bank of Gabor kernels at each of
            the facial landmarks. The default is all 0's.
        """
        self.features = features
        """
        Responses of the filtering with the bank of Gabor kernels at each of the
        facial landmarks. The Gabor bank used has 32 kernels and there are 68
        landmarks, hence this is a vector of 2176 values (32 x 68).
        """

    #---------------------------------------------
    def copy(self):
        """
        Deep copies the data of this object.

        Deep copying means that no mutable attribute (like tuples or lists) in
        the new copy will be shared with this instance. In that way, the two
        copies can be changed independently.

        Returns
        -------
        ret: GaborData
            New instance of the GaborData class deep copied from this instance.
        """
        return GaborData(self.features.copy())

    #---------------------------------------------
    def isEmpty(self):
        """
        Check if the object is empty.

        Returns
        ------
        response: bool
            Indication on whether this object is empty.
        """
        return all(v == 0 for v in self.features5)

class FaceEmotionDetector:
    _detector = None
    _predictor = None

    def __init__(self):
        # The instance of the face detector.
        self._bank = GaborBank()
        # The instance of the bank of Gabor filters.
        # self._emotionsDet = EmotionsDetector()
        # The instance of the emotions detector.
        self._face = FaceData()
        # Data of the last face detected.
        # self._emotions = OrderedDict()
        # Data of the last emotions detected.

    def detect(self, image, downSampleRatio = None):
        """
        Tries to automatically detect a face in the given image.

        This method uses the face detector/predictor from the dlib package (with
        its default face model) to detect a face region and 68 facial landmarks.
        Even though dlib is able to detect more than one face in the image, for
        the current purposes of the fsdk project only a single face is needed.
        Hence, only the biggest face detected (estimated from the region size)
        is considered.

        Parameters
        ------
        image: numpy.array
            Image data where to search for the face.
        downSampleRatio: float

        Returns
        ------
        result: bool
            Indication on the success or failure of the facial detection.
        face: FaceData
            Instance of the FaceData class with the region and landmarks of the
            detected face, or None if no face was detected.
        """

        #####################
        # Setup the detector
        #####################

        # Initialize the static detector and predictor if this is first use
        if self._detector is None or self._predictor is None:
            self._detector = dlib.get_frontal_face_detector()

            faceModel = os.path.abspath('{}/models/face_model.dat' \
                            .format(os.path.dirname(__file__)))
            self._predictor = dlib.shape_predictor(faceModel)

        #####################
        # Performance cues
        #####################

        # If requested, scale down the original image in order to improve
        # performance in the initial face detection
        if downSampleRatio is not None:
            detImage = cv2.resize(image, (0, 0), fx=1.0 / downSampleRatio,
                                                 fy=1.0 / downSampleRatio)
        else:
            detImage = image

        #####################
        # Face detection
        #####################

        # Detect faces in the image
        detectedFaces = self._detector(detImage, 1)
        if len(detectedFaces) == 0:
            self._ret = False
            self._face = None
        else:
            self._ret = True
        # No matter how many faces have been found, consider only the first one
            region = detectedFaces[0]
            # If downscaling was requested, scale back the detected region so the
            # landmarks can be proper located on the image in full resolution
            if downSampleRatio is not None:
                region = dlib.rectangle(region.left() * downSampleRatio,
                                        region.top() * downSampleRatio,
                                        region.right() * downSampleRatio,
                                        region.bottom() * downSampleRatio)

            # Fit the shape model over the face region to predict the positions of
            # its facial landmarks
            faceShape = self._predictor(image, region)

            # Update the object data with the predicted landmark positions and
            # their bounding box (with a small margin of 10 pixels)
            self._face.landmarks = np.array([[p.x, p.y] for p in faceShape.parts()])

            margin = 10
            x, y, w, h = cv2.boundingRect(self._face.landmarks)
            self._face.region = (
                        max(x - margin, 0),
                        max(y - margin, 0),
                        min(x + w + margin, image.shape[1] - 1),
                        min(y + h + margin, image.shape[0] - 1)
                        )

            # Crop just the face region
            image, self._face = self._face.crop(image)

            # Filter it with the Gabor bank
            responses = self._bank.filter(image)

            # Detect the prototypic emotions based on the filter responses
            #self._emotions = self._emotionsDet.detect(face, responses)
            
            #return self._emotions
        return self._ret, self._face
    def draw(self, frame):
        output = self._face.draw(frame)
        return output
        # """
        # Draws the detected data of the given frame image.

        # Parameters
        # ----------
        # frame: numpy.ndarray
        #     Image where to draw the information to.
        # """
        # # Font settings
        # font = cv2.FONT_HERSHEY_SIMPLEX
        # scale = 0.5
        # thick = 1
        # glow = 3 * thick

        # # Color settings
        # black = (0, 0, 0)
        # white = (255, 255, 255)
        # yellow = (0, 255, 255)
        # red = (0, 0, 255)

        # empty = True

        # # Plot the face landmarks and face distance
        # x = 5
        # y = 0
        # w = int(frame.shape[1]* 0.2)

        # try:
        #     face = self._face
        #     empty = face.isEmpty()
        #     #face.draw(frame)
        # except:
        #     pass

        # Plot the emotion probabilities
        # try:
        #     emotions = self._emotions
        #     if empty:
        #         labels = []
        #         values = []
        #     else:
        #         labels = list(emotions.keys())
        #         values = list(emotions.values())
        #         bigger = labels[values.index(max(values))]

        #         # Draw the header
        #         text = 'emotions'
        #         size, _ = cv2.getTextSize(text, font, scale, thick)
        #         y += size[1] + 20

        #         cv2.putText(frame, text, (x, y), font, scale, black, glow)
        #         cv2.putText(frame, text, (x, y), font, scale, yellow, thick)

        #         y += 5
        #         cv2.line(frame, (x,y), (x+w,y), black, 1)

        #     size, _ = cv2.getTextSize('happiness', font, scale, thick)
        #     t = size[0] + 20
        #     w = 150
        #     h = size[1]
        #     for l, v in zip(labels, values):
        #         lab = '{}:'.format(l)
        #         val = '{:.2f}'.format(v)
        #         size, _ = cv2.getTextSize(l, font, scale, thick)

        #         # Set a red color for the emotion with bigger probability
        #         color = red if l == bigger else yellow

        #         y += size[1] + 15

        #         p1 = (x+t, y-size[1]-5)
        #         p2 = (x+t+w, y-size[1]+h+5)
        #         cv2.rectangle(frame, p1, p2, black, 1)

        #         # Draw the filled rectangle proportional to the probability
        #         p2 = (p1[0] + int((p2[0] - p1[0]) * v), p2[1])
        #         cv2.rectangle(frame, p1, p2, color, -1)
        #         cv2.rectangle(frame, p1, p2, black, 1)

        #         # Draw the emotion label
        #         cv2.putText(frame, lab, (x, y), font, scale, black, glow)
        #         cv2.putText(frame, lab, (x, y), font, scale, color, thick)

        #         # Draw the value of the emotion probability
        #         cv2.putText(frame, val, (x+t+5, y), font, scale, black, glow)
        #         cv2.putText(frame, val, (x+t+5, y), font, scale, white, thick)
        # except Exception as e:
            # print(e)
            # pass