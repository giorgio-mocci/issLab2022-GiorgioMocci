package it.unibo.radarSystem22.main;

import radarPojo.radarSupport;

import java.io.BufferedReader;
import java.io.DataInputStream;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.*;
import java.util.UUID;

import org.eclipse.paho.client.mqttv3.IMqttClient;
import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallback;
import org.eclipse.paho.client.mqttv3.MqttClient;
import org.eclipse.paho.client.mqttv3.MqttConnectOptions;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;
import org.eclipse.paho.client.mqttv3.persist.MemoryPersistence;

public class RadarUsageMainTCP {

	public void doJob() { // funzione che fa andare il server con java socker

		try {
			ServerSocket serverSocket = new ServerSocket(6666);
			while (true) {
				Socket clientSocket = serverSocket.accept();
				BufferedReader distance = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));
				String distanza = distance.readLine();
				radarSupport.update("" + distanza, "0");
			}

		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}

	}

	public static void main(String[] args) throws MqttException {
		System.out.println("start RADAR TCP");
		radarSupport.setUpRadarGui();
		new RadarUsageMainTCP().doJob();

	}
}
