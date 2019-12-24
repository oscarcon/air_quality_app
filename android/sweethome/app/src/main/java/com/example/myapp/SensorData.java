package com.example.myapp;

import android.app.Application;

public class SensorData {
    private static final SensorData ourInstance = new SensorData();
    public static SensorData getInstance() {
        return ourInstance;
    }

    private String temp1 = "", temp2 = "", humid1 = "", humid2 = "", light1 = "", light2 = "", gas1 = "", gas2 = "";

    public void setTemp1(String value) {
        this.temp1 = value;
    }
    public String getTemp1() {
        return temp1;
    }
    public void setTemp2(String value) {
        this.temp2 = value;
    }
    public String getTemp2() { return temp2; }

    public void setHumid1(String value) { this.humid1 = value; }
    public String getHumid1() {
        return humid1;
    }
    public void setHumid2(String value) {
        this.humid2 = value;
    }
    public String getHumid2() { return humid2; }

    public void setLight1(String value) { this.light1 = value; }
    public String getLight1() { return light1; }
    public void setLight2(String value) {
        this.light2 = value;
    }
    public String getLight2() {
        return light2;
    }


}
