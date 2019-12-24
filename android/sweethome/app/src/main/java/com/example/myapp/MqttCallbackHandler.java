package com.example.myapp;

import android.util.Log;
import android.widget.TextView;
import androidx.appcompat.app.AppCompatActivity;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import com.example.myapp.SensorData;

public class MqttCallbackHandler implements MqttCallback {
    @Override
    public void connectionLost(Throwable throwable) {
    }
    @Override
    public void messageArrived(String topic, MqttMessage mqttMessage) throws Exception {
        Log.w("Received message:", topic + ":" + mqttMessage.toString());
        if (topic.contains("/sensor_data/living_room")) {
            if (topic.contains("temperature")) {
                SensorData.getInstance().setTemp1(mqttMessage.toString());
            }
            else if (topic.contains("humidity")) {
                SensorData.getInstance().setHumid1(mqttMessage.toString());
            }
            else if (topic.contains("light")) {
                SensorData.getInstance().setLight1(mqttMessage.toString());
            }
        }
        else if (topic.contains("/sensor_data/kitchen")) {
            if (topic.contains("temperature")) {
                SensorData.getInstance().setTemp2(mqttMessage.toString());
            }
            else if (topic.contains("humidity")) {
                SensorData.getInstance().setHumid2(mqttMessage.toString());
            }
            else if (topic.contains("light")) {
                SensorData.getInstance().setLight2(mqttMessage.toString());
            }
        }
    }
    @Override
    public void deliveryComplete(IMqttDeliveryToken iMqttDeliveryToken) {
    }
}
