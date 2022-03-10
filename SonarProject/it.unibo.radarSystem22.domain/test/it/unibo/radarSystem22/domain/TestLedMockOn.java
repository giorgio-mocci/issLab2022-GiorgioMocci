package it.unibo.radarSystem22.domain;

import it.unibo.radarSystem22.domain.intefaces.ILed;
import it.unibo.radarSystem22.domain.mock.ledMock;

import static org.junit.Assert.assertTrue;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;


public class TestLedMockOn {
	  @Before
	  public void up(){ System.out.println("up"); }
	  @After
	  public void down(){ System.out.println("down"); }
	  @Test
	  public void testLedMock() {
	    
		System.out.println("Test Led Mock");

	    ILed led = new ledMock();
	    led.turnOn();
	    assertTrue(  led.getState() );   
	    
	    

	  
	  }
	}
