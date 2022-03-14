package it.unibo.radarSystem22.domain;

import static org.junit.Assert.*;

import java.util.Random;

import org.junit.After;
import org.junit.Assert;
import org.junit.Before;
import org.junit.Test;

import it.unibo.radarSystem22.domain.intefaces.ISonar;
import it.unibo.radarSystem22.domain.mock.SonarMock;
import junit.framework.ComparisonFailure;

public class TestSonarMock {

	private long startTime;
	private final int startCount = 90;
	

	@Test
	public void test() throws InterruptedException {

		ISonar sonar = new SonarMock();
		// Activate Sonar
		sonar.activate();
		// Start counting
		this.startTime = System.currentTimeMillis();
		assertTrue(sonar.isActive());
		// check the misured distance
		
		int randomValSleepTime = new Random().nextInt(1000);
		Thread.sleep(randomValSleepTime);
		long timePassedSinceStart = System.currentTimeMillis() - this.startCount;
		int calculatedDistance = (int) (this.startCount - (timePassedSinceStart / 250));

		// Test distance
		try {
			Assert.assertEquals(new Distance(calculatedDistance).getVal(), sonar.getDistance().getVal());
		} catch (ComparisonFailure e) {
			System.out.println(e.getMessage());
		}
		
		

		// Deactivate Sonar
		sonar.deactivate();
		assertFalse(sonar.isActive());

	}

}
