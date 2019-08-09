/***
* Name: CircularBarChart
* Author: Huy
* Description: 
* Tags: Tag1, Tag2, TagN
***/

model CircularBarChart

/* Insert your model definition here */
global {
	int radius <- 20;
	int bar_side <- 2;
	float d <- 50*bar_side;
	list<list<float>> events;
	file csv <- csv_file("../includes/data.csv");
	geometry shape <- cube(200);
	init {
		matrix data <- matrix(csv);
		loop i from:0 to:(data.rows-1)/100 {
			list<float> temp;
			loop j from:0 to:data.columns-1{
				float x <- data[j,i];
				add (x + 10)*10 to:temp;
			}
			add temp to:events;
		}
		int k <- 0;
		loop el over:events {
			Chart chart;
			int len <- length(el);
			float _angle <- 0.0;
			
			create Chart {
				color <- #blue;
				show <- false;
				chart <- self;
			}

//			create Chart;
//			Chart chart <- Chart[0];
//			int k <- 0;
//			list<int> el <- events[0];
//			int len <- length(el);
//			float _angle <- 0.0;			
			loop i from:0 to:len-1 {
				create Bar {
					angle <- _angle;
					height <- el[i];
					start <- {d*k,(radius)*sin(angle),(radius)*cos(angle)};
					add self to:chart.barList;
				}
				_angle <- _angle + 360/len;
			}
			k <- k + 1;
		}
	} // end init
	reflex default {
		int a_rand <- rnd(1000);
		int len <- length(Chart);
		int i <- cycle;
		if (i < len) {
			Chart[i].show <- true;
			if (a_rand > 20 and a_rand mod 7 = 0) {
				Chart[i].color <- #red;
			}
		}
	}
	
}

species Animation {
	
}

species Chart {
	list<Bar> barList;
	bool show;
	rgb color;
	aspect default {
		loop bar over:barList {
			if (show = true) {
				draw box(bar_side,bar_side/2,bar.height) at: bar.start rotate:bar.angle::{-1,0,0} color: color;
			}
		}
	}
}
species Bar {
	float height;
	point start;
	float angle;
	//rgb color;
	aspect default {
		draw shape;
	}
}

//species Test {
//	aspect default {
//		draw shape;
//	}
//}

experiment Char3D type: gui{
	
	output {
		display View1 type:opengl {
			species Chart aspect:default;
//			graphics "env" {
//				loop i from:0 to:49 {
//					draw box(bar_side,bar_side,100) at: {0,0,0} rotate:360/50*i::{1,0,0};
//				}
//				
//			}
		}
	}
}