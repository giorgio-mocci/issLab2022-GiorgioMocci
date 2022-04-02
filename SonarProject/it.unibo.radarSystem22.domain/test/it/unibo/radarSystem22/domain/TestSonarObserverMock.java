package it.unibo.radarSystem22.domain;
import static org.junit.Assert.assertTrue;
import org.junit.*;

import it.unibo.radarSystem22.domain.interfaces.ISonar;
import it.unibo.radarSystem22.domain.mock.SonarObservableMock;
import it.unibo.radarSystem22.domain.observer.SonarObserver;
import it.unibo.radarSystem22.domain.observer.SonarObserverBroker;
import it.unibo.radarSystem22.domain.utils.BasicUtils;
import it.unibo.radarSystem22.domain.utils.DomainSystemConfig;
 

public class TestSonarObserverMock {
	
	private static int DTESTING1 = 50;
	private static int DTESTING2 = 100;
	
	@Before
	public void up() {
		System.out.println("up");
	}
	
	@After
	public void down() {
		System.out.println("down");		
	}	
	
	@Test 
	public void testSonarMock() {
		DomainSystemConfig.simulation = true;
		DomainSystemConfig.testing    = false;
		DomainSystemConfig.sonarDelay = 10;		//quite fast generation ...		
		
		ISonar sonar = new SonarObservableMock();
		SonarObserverBroker broker = ((SonarObservableMock) sonar).getSonarObserverBroker();
		
		SonarObserver ob1 = new SonarObserver("ob1");		
		SonarObserver ob2 = new SonarObserver("ob2");
		broker.AddObserver(ob1);
		broker.AddObserver(ob2);
		
		((SonarObservableMock) sonar).sonarSetDistance(DTESTING1);		
		assertTrue(ob1.getVal() == DTESTING1);
		assertTrue(ob2.getVal() == DTESTING1);
		
		
		
		((SonarObservableMock) sonar).sonarSetDistance(DTESTING2);		
		assertTrue(ob1.getVal() == DTESTING2);
		assertTrue(ob2.getVal() == DTESTING2);
		
		
		
		
		sonar.activate();		
 		while( sonar.isActive() ) { BasicUtils.delay(1000);} //to avoid premature exit
 	}
	
 
}
