package it.unibo.radarSystem22.domain.concrete;

import java.io.BufferedReader;
import java.io.InputStreamReader;

import it.unibo.radarSystem22.domain.Distance;
import it.unibo.radarSystem22.domain.interfaces.ISonar;
import it.unibo.radarSystem22.domain.models.SonarObservableModel;
import it.unibo.radarSystem22.domain.observer.SonarObserverBroker;
import it.unibo.radarSystem22.domain.utils.ColorsOut;
import it.unibo.radarSystem22.domain.utils.DomainSystemConfig;

public class SonarObservableConcrete extends SonarObservableModel implements ISonar{

	private  BufferedReader reader ;
	private Process p ;
	
	@Override
	protected void sonarSetUp() {
		curVal = new Distance(90);
		broker = new SonarObserverBroker();
		
	}
	
	public void activate() {
		ColorsOut.out("SonarConcrete | activate ");
		if (p == null) {
			try {
				p = Runtime.getRuntime().exec("sudo ./SonarAlone"); // necessario all'interno del raspberry chmod +x SonarAlone
				reader = new BufferedReader(new InputStreamReader(p.getInputStream()));
				ColorsOut.out("SonarConcrete | sonarSetUp done");
			} catch (Exception e) {
				ColorsOut.outerr("SonarConcrete | sonarSetUp ERROR " + e.getMessage());
			}
		}
		super.activate();
	}

	@Override
	protected void sonarProduce( ) {
        try {
			String data = reader.readLine();
			if( data == null ) return;
			int v = Integer.parseInt(data);
			ColorsOut.out("SonarConcrete | v=" + v );
			int lastSonarVal = curVal.getVal();
			if( lastSonarVal != v && v < DomainSystemConfig.sonarDistanceMax) {	
				//Eliminiamo dati del tipo 3430 //TODO: filtri in sottosistemi a stream
  	 			updateDistance( v );	 			
			}
       }catch( Exception e) {
       		ColorsOut.outerr("SonarConcrete |  " + e.getMessage() );
       }		
	}
 
	@Override
	public void deactivate() {
		ColorsOut.out("SonarConcrete | deactivate", ColorsOut.GREEN);
	    curVal = new Distance(90);
		if( p != null ) {
			p.destroy();  //Block the runtime process
			p=null;
		}
		super.deactivate();
 	}

}
