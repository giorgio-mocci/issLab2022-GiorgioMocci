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



public class RadarUsageMainOLD implements MqttCallback {
 	
	/** The broker url. */
	private static final String brokerUrl ="tcp://192.168.1.12:1883";
	
	/* The client id. */
	private static final String clientId = "clientId";

	/** The topic. */
	private static final String topic = "radar";
	
	public void doJob() { //funzione che fa andare il server con java socker
		
 		
 		try {
			ServerSocket serverSocket = new ServerSocket(6666);		
			 while(true)
			 {				 
				 Socket clientSocket  = serverSocket.accept();
				 BufferedReader distance = new BufferedReader(new InputStreamReader(clientSocket.getInputStream()));			
				 String distanza = distance.readLine();				 	
				 radarSupport.update(""+distanza , "0");							 		
			 }
			 
			
			
			 
			
		} catch (IOException e) {
			// TODO Auto-generated catch block
			e.printStackTrace();
		}
 		
 		
		
 	
 	}
	
	public void subscribe(String topic) {
		//	logger file name and pattern to log
		MemoryPersistence persistence = new MemoryPersistence();

		try
		{

			MqttClient sampleClient = new MqttClient(brokerUrl, clientId, persistence);
			MqttConnectOptions connOpts = new MqttConnectOptions();
			connOpts.setCleanSession(true);

			System.out.println("checking");
			System.out.println("Mqtt Connecting to broker: " + brokerUrl);

			sampleClient.connect(connOpts);
			System.out.println("Mqtt Connected");

			sampleClient.setCallback( this);
			sampleClient.subscribe(topic);

			System.out.println("Subscribed");
			System.out.println("Listening");

		} catch (MqttException me) {
			System.out.println(me);
		}
	}

	 //Called when the client lost the connection to the broker
	public void connectionLost(Throwable arg0) {
		System.out.println("CONNCETIONS LOST!");
	}

	//Called when a outgoing publish is complete
	public void deliveryComplete(IMqttDeliveryToken arg0) {
		System.out.println("outgoing publish is complete!");
	}

	public void messageArrived(String topic, MqttMessage message) throws Exception {
		
		 radarSupport.update(""+message.toString() , "0");
		
		System.out.println("| Topic:" + topic);
		System.out.println("| Message: " +message.toString());
		System.out.println("-------------------------------------------------");

	}


	
	public static void main(String[] args) throws MqttException {
		System.out.println("start RADAR2 ");
		radarSupport.setUpRadarGui();
	//	new RadarUsageMain().doJob();
		String publisherId = UUID.randomUUID().toString();
		new RadarUsageMainOLD().subscribe(topic);		
	}
}
