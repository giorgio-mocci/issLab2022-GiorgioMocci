package it.unibo.radarSystem22.domain.observer;

import java.util.ArrayList;
import java.util.List;

import it.unibo.radarSystem22.domain.interfaces.IDistance;
import it.unibo.radarSystem22.domain.interfaces.ISonarObserver;

public class SonarObserverBroker {

	private IDistance curVal;
	private List<ISonarObserver> observers = new ArrayList<ISonarObserver>();
	
	public void AddObserver(ISonarObserver observer) {
		this.observers.add(observer);
	}
	
	public void RemoveObserver(ISonarObserver observer) {
		this.observers.remove(observer);
	}
	
	public void Publish(IDistance curVal) {
		this.curVal = curVal;
		for(ISonarObserver observer : this.observers)
		{
			
			observer.update(curVal);
			
		}
		
	}

}
