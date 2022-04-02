package it.unibo.radarSystem22.domain.observer;

import it.unibo.radarSystem22.domain.Distance;
import it.unibo.radarSystem22.domain.interfaces.IDistance;
import it.unibo.radarSystem22.domain.interfaces.ISonarObserver;

public class SonarObserver implements ISonarObserver{

	private IDistance distance;
	private String ID;
	
	public SonarObserver(String iD) {
		super();
		ID = iD;
		this.distance = new Distance(-1);
	}

	@Override
	public void update(IDistance dist) {
		this.distance= dist;
		System.out.println("Observer "+ ID + " valore aggiornato: "+this.getVal());
	}

	@Override
	public int getVal() {
		return distance.getVal();
	}

}
