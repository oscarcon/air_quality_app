package com.example.myapp;

import android.os.Bundle;

import com.example.myapp.ui.main.PlaceholderFragment;
import com.example.myapp.ui.main.PlaceholderFragment2;
import com.google.android.material.floatingactionbutton.FloatingActionButton;
import com.google.android.material.snackbar.Snackbar;
import com.google.android.material.tabs.TabLayout;

import androidx.viewpager.widget.ViewPager;
import androidx.appcompat.app.AppCompatActivity;

import android.os.Handler;
import android.util.Log;
import android.view.LayoutInflater;
import android.view.View;
import android.widget.TextView;

import com.example.myapp.ui.main.SectionsPagerAdapter;
import org.eclipse.paho.client.mqttv3.*;
import org.eclipse.paho.android.service.*;

public class MainActivity extends AppCompatActivity {
    Handler handler = new Handler();
    private Runnable periodicUpdate = new Runnable () {
        public void run() {
            // scheduled another events to be in 10 seconds later
            handler.postDelayed(periodicUpdate, 1000);
//            setContentView(R.layout.activity_main);
            TextView text;
            text = (TextView)findViewById(R.id.textView1);
            text.setText(String.valueOf(SensorData.getInstance().getTemp1()));
            text = (TextView)findViewById(R.id.textView2);
            text.setText(String.valueOf(SensorData.getInstance().getHumid1()));
            text = (TextView)findViewById(R.id.textView3);
            text.setText(String.valueOf(SensorData.getInstance().getLight1()));
//            text = (TextView)findViewById(R.id.textView4);
//            text.setText(String.valueOf(SensorData.getInstance().getTemp1()));
            text = (TextView)findViewById(R.id.textView5);
            text.setText(String.valueOf(SensorData.getInstance().getTemp2()));
            text = (TextView)findViewById(R.id.textView6);
            text.setText(String.valueOf(SensorData.getInstance().getHumid2()));
            text = (TextView)findViewById(R.id.textView7);
            text.setText(String.valueOf(SensorData.getInstance().getLight2()));
            Log.w("DEBUG", "Routine");
        }
    };
    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);
        SectionsPagerAdapter sectionsPagerAdapter = new SectionsPagerAdapter(this, getSupportFragmentManager());
        ViewPager viewPager = findViewById(R.id.view_pager);
        sectionsPagerAdapter.addFrag(new PlaceholderFragment(), "Living Room");
        sectionsPagerAdapter.addFrag(new PlaceholderFragment2(), "Kitchen");

        viewPager.setAdapter(sectionsPagerAdapter);
        TabLayout tabs = findViewById(R.id.tabs);
        tabs.setupWithViewPager(viewPager);
        FloatingActionButton fab = findViewById(R.id.fab);

        fab.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View view) {
                Snackbar.make(view, "Replace with your own action", Snackbar.LENGTH_LONG)
                        .setAction("Action", null).show();
            }
        });
        View view = LayoutInflater.from(this).inflate(R.layout.fragment_main_2, null);
//        viewPager.setCurrentItem();
        // Start MQTT client
        String clientId = MqttClient.generateClientId();
        final MqttAndroidClient client =
                new MqttAndroidClient(this.getApplicationContext(), "tcp://m14.cloudmqtt.com:17331",
                        clientId);

        try {
            MqttConnectOptions opts = new MqttConnectOptions();
            opts.setUserName("oozxmhuj");
            opts.setPassword("ZJFq_THcgUX0".toCharArray());
            IMqttToken token = client.connect(opts);
            token.setActionCallback(new IMqttActionListener() {
                @Override
                public void onSuccess(IMqttToken asyncActionToken) {
                    // We are connected
                    Log.d("MQTT", "onSuccess");
//                    String topic = "foo/bar";
//                    String payload = "the payload";
//                    byte[] encodedPayload = new byte[0];
//                    try {
//                        encodedPayload = payload.getBytes("UTF-8");
//                        MqttMessage message = new MqttMessage(encodedPayload);
//                        client.publish(topic, message);
//                    } catch (UnsupportedEncodingException | MqttException e) {
//                        e.printStackTrace();
//                    }
                    try {
                        IMqttToken subToken = client.subscribe("#", 1);
                        subToken.setActionCallback(new IMqttActionListener() {
                            @Override
                            public void onSuccess(IMqttToken asyncActionToken) {
                                // The message was published
                                Log.w("SUB","Subscribe success");
                            }

                            @Override
                            public void onFailure(IMqttToken asyncActionToken,
                                                  Throwable exception) {
                                // The subscription could not be performed, maybe the user was not
                                // authorized to subscribe on the specified topic e.g. using wildcards

                            }
                        });

                    } catch (MqttException e) {
                        e.printStackTrace();
                    }
                }

                @Override
                public void onFailure(IMqttToken asyncActionToken, Throwable exception) {
                    // Something went wrong e.g. connection timeout or firewall problems
                    Log.d("MQTT", "onFailure");

                }
            });
            client.setCallback(new MqttCallbackHandler());

        } catch (MqttException e) {
            e.printStackTrace();
        }
        findViewById(R.id.textView1);
        handler.postDelayed(periodicUpdate,1000);
    }
}



