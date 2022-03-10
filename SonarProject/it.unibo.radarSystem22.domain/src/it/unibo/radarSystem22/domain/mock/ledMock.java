package it.unibo.radarSystem22.domain.mock;

import it.unibo.radarSystem22.domain.intefaces.ILed;

public class ledMock implements ILed{

	private boolean state;
	
	@Override
	public void turnOn() {
		this.state = true;
		
	}

	@Override
	public void turnOff() {
		this.state = false;
		
	}

	@Override
	public boolean getState() {
		return this.state;
	}

}
