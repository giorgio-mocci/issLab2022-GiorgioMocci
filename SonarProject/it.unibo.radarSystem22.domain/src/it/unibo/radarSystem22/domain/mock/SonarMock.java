package it.unibo.radarSystem22.domain.mock;

import it.unibo.radarSystem22.domain.Distance;
import it.unibo.radarSystem22.domain.intefaces.IDistance;
import it.unibo.radarSystem22.domain.intefaces.ISonar;

public class SonarMock implements ISonar {

	private boolean state;
	private long startTime;
	private final int startCount = 90;

	@Override
	public void activate() {
		this.state = true;
		this.startTime = System.currentTimeMillis();
	}

	@Override
	public void deactivate() {
		this.state = false;
		this.startTime = -1;

	}

	@Override
	public IDistance getDistance() {
		if (!this.state)
			return new Distance(-1);
		long timePassedSinceStart = System.currentTimeMillis() - this.startCount;
		int calculatedDistance = (int) (this.startCount - (timePassedSinceStart / 250));
		if (calculatedDistance < 0)
			calculatedDistance = 0;
		return new Distance(calculatedDistance);
	}

	@Override
	public boolean isActive() {
		return this.state;
	}

}
