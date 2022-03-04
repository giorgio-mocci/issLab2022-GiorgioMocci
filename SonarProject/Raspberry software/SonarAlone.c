#include <sstream>

#include <iostream>
#include <wiringPi.h>
#include <fstream>
#include <cmath>
#include <stdio.h>
#include <sys/socket.h>
#include <arpa/inet.h>
#include <unistd.h>
#include <string.h>
#define PORT 6666


#define TRIG 0
#define ECHO 2

#define CLOSE 18
#define MEDIUM 21
#define FAR 60

#define POS_LEFT 0.055
#define POS_RIGHT 0.24
#define POS_FORWARD 0.14
#define SSTR( x ) static_cast< std::ostringstream & >( \
        ( std::ostringstream() << std::dec << x ) ).str()

using namespace std;
/*
g++  SonarAlone.c -l wiringPi -o  SonarAlonec
 */
void setup() {
	//cout << "setUp " << endl;
	wiringPiSetup();
	pinMode(TRIG, OUTPUT);
	pinMode(ECHO, INPUT);
	//TRIG pin must start LOW
	digitalWrite(TRIG, LOW);
	delay(30);
}

int getCM() {
	//Send trig pulse
	digitalWrite(TRIG, HIGH);
	delayMicroseconds(20);
	digitalWrite(TRIG, LOW);

	//Wait for echo start
	while(digitalRead(ECHO) == LOW);

	//Wait for echo end
	long startTime = micros();
	while(digitalRead(ECHO) == HIGH);
	long travelTime = micros() - startTime;

	//Get distance in cm
	int distance = travelTime / 58;

	return distance;
}


void send(int cm)
{
  int sock = 0, valread;
      struct sockaddr_in serv_addr;
      ;
      char buffer[1024] = {0};
      if ((sock = socket(AF_INET, SOCK_STREAM, 0)) < 0)
      {
          printf("\n Socket creation error \n");
  
      }

      serv_addr.sin_family = AF_INET;
      serv_addr.sin_port = htons(PORT);

      // Convert IPv4 and IPv6 addresses from text to binary form
      if(inet_pton(AF_INET, "192.168.1.5", &serv_addr.sin_addr)<=0)
      {
          printf("\nInvalid address/ Address not supported \n");
      }
      if (connect(sock, (struct sockaddr *)&serv_addr, sizeof(serv_addr)) < 0)
      {
          printf("\nConnection Failed \n");
//          return -1;

      }
      char *hello = "Hello from Giorgio\n";

	char snum[10];

     // convert 123 to string [buf]
 	     
  		
while(1)
{
	    cm=getCM();
		if (cm <= 20)system("/home/pi/Desktop/ledBlink.sh");
		else system("/home/pi/Desktop/ledOff.sh");
                send(sock , &cm , sizeof(int) , 0 );
		printf("message sent %d \n",cm);
                delay(100);
}

}

int main(void) {
	
	setup();
	send(1);

 	return 0;
}

