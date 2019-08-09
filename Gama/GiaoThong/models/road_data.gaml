/**
* Name: He thong giao thong thanh pho Da Nang
* Author: TQH
* Description:
* Tags: traffic system
*/

model danang_traffic_database

global {
	file shape_file_roads <- file("../includes/Tim_duong.shp");
	file hethong_csv <- csv_file("../includes/hethongGT.csv",true);
	geometry shape <- envelope(shape_file_roads);	// global shape for road
	//geometry shape <- cube(200);	// global shape for traffic system
	float step <- 10 #mn;
	int nb_people <- 100;
	int mode <- 0;
	int R <- 50;
	list<list<cautruc>> tree;
	
	action create_subs_aroud(cautruc ct, int nb_subs) {
		write "Hello";
	}
	

	init {
		create cautruc from: hethong_csv with: [
			shape::sphere(int(get("r_sphere"))),
			id::int(get("id")),
			ten::string(get("name")),
			pre_id::int(get("pre_id")),
			color::#blue,
			r::float(get("r")),
			phi::float(get("phi")),
			theta::float(get("theta")),
			stage::int(get("stage"))			
		] 
		{
			
		}
		
		cautruc[0].location <- {100,100,0};
		cautruc[0].color <- #red;
		loop c over: cautruc {
			loop ca over:cautruc {
				if (ca.pre_id = c.id) {
					c.nexts << ca;
				}
			}
		}
		loop c over:cautruc {
			if (!empty(c.nexts)) {
				loop cc over:c.nexts {
					cc.nb_subs <- length(cc.nexts);
					cc.x <- cc.r*cos(cc.phi)*sin(cc.theta);
					cc.y <- cc.r*sin(cc.phi)*sin(cc.theta);
					cc.z <- cc.r*cos(cc.theta);
					cc.location <- {c.location.x + cc.x, c.location.y + cc.y, c.location.z + cc.z};
				}
			}
		}
		
//		create cautruc {
//			location <- {0,0,0};
//			shape <- sphere(10);
//			color <- #blue;
//			int counter;
//			create cautruc number: 4 {
//				color <- #transparent;
//				if (counter = 0) {
//					theta <- 0.0;
//					phi <- 0.0;
//				}
//				else {
//					theta <- 120.0;
//					phi <- (counter-1)*120.0;
//				}
//				
//				x <- R*cos(phi)*sin(theta);
//				y <- R*sin(phi)*sin(theta);
//				z <- R*cos(theta);
//				location <- {x,y,z};
//				shape <- sphere(10);
//				myself.nexts << self;
//				counter <- counter + 1;
//			}
//		}
		
		
		create road from: shape_file_roads with:[roadname::string(read("Ten")), id::int(read("OBJECTID"))];
		create db number: length(road) {
			road rd <- one_of(road);
			link_rd <- rd;
			location <- {rd.location.x, rd.location.y, rd.location.z - 50};
			shape <- box(20,20,10);
			ask rd {
				link_db <- myself;
			}
//			create data_block number: rnd(2) + 3 {
//				shape <- box(20,20,10);
//				link_db <- myself;
//				myself.list_data << self;
//			}
//			create data_block number: rnd(2) + 3 {
//				shape <- box(20,20,10);
//				link_db <- myself;
//				//myself.list_data << self;
//				
//			}
			if (rd.id = 406) {
				rd.color <- #red;
				rd.roadname <- "Ly Thuong Kiet";
				
				loop interval from:0 to: 2 {
					list<data_block> lst;
					if (interval = 0) {
						create data_block number: 3 {
							shape <- box(20,20,10);
							link_db <- myself;
							lst << self;
						}
					}
					else {
						create data_block number: 2 {
							shape <- box(20,20,10);
							link_db <- myself;
							lst << self;
						}
					}
					list_data << lst;
				}
			
				int i <- 0;
				point start_location <- {location.x-30, location.y, location.z-30};
				loop lst over: list_data {
					point current_location <-{start_location.x+i*30, start_location.y,start_location.z};
					int k <- 0;
					loop block over:lst {
						block.url <- "http://safehorizons.ddns.net:3008/giaothong/";
						block.location <- {current_location.x, current_location.y,current_location.z-k*30};
						k <- k + 1;
					}
					i <- i + 1;
				}
			}
			else {
				do die;
			}
		}
	}
}
species data_block {
	string url;
	rgb color <- #green;
	db link_db;
	
	int level;
	action action_open_url {
		color <- #darkblue;
	}
	aspect view {
		draw shape color: color;
		//draw "text" size: 6 color:#darkblue;
	}
}

species cautruc {
	string ten;
	int id;
	int pre_id;
	int stage;
	list<cautruc> nexts;
	bool show <- false;
	rgb color;
	int nb_subs;
	float r;
	float theta;
	float phi;
	float x;
	float y;
	float z;
	
	action show_subs {
		show <- !(show);
//		loop s over:nexts {
//			if (show)
//			{
//				s.color <- #red;
//			}
//			else 
//			{
//				s.color <- #transparent;
//				loop ss over: s.nexts {
//					ss.color <- #transparent;
//				}
//				
//			}
//		}
	}
	
	user_command "show" action:show_subs;
	
	aspect sphere3d {
		nb_subs <- length(nexts);
		draw shape color: color;
//		loop s over:nexts {
//				draw line([self.location,s.location]) color: #black;
//		}
		//draw ten color:#black at: {location.x/2,location.y};
		if (show) {
			loop s over:nexts {
				if (empty(s.nexts) = true) {
					s.color <- #green;
				} else {
					s.color <- #blue;
				}
				point x <- {self.location.x, self.location.y, self.shape.height/2};
				point y <- {s.location.x, s.location.y, s.shape.height/2};
				draw line([x,y]) color: #gray width: 10 - stage*1.5;
				draw s.ten rotate: -90::{1,0,0} color:#black at: {s.location.x,s.location.y,30};
			}
//			if (empty(nexts) = true) {
//				color <- #green;
//			} 
//			else {
//				color <- #blue;
//			}
		}
		else {
			if (id != 0) {
				color <- #transparent;
			}
			else {
				draw ten rotate: -90::{1,0,0} color:#black at: {location.x/2,location.y,30};
			}
//			loop s over:nexts {
//				s.color <- #transparent;
//			}
		}
	}
}

species db {
	rgb color <- #green;
	rgb line_color <- #green;
	road link_rd;
	list<list<data_block>> list_data;
	aspect view {
		draw shape color: color;
		draw line([self.location,link_rd.location]) color: line_color width:2;
		if (!empty(list_data)) {
			loop bl over:list_data {
				point ptop <- {bl[0].location.x, bl[0].location.y, bl[0].location.z + self.shape.depth/2};
				draw line([self.location,ptop]) color: line_color width:2;
				point temp <- bl[0].location;
				loop index from:1 to: 2 {
					draw line([bl[index].location, temp]) color: line_color width:2;
					temp <- bl[index].location;
				}
			}
		}
		
		//draw string(db index_of self) font:font("Arial",30,#plain) color:;
	}
	aspect sphere3d {
		
	}
}

species road  {
	rgb color <- #blue;
	string roadname;
	int id;
	db link_db;
	aspect base {
		if (self.id = 406) {
			draw roadname size:1 color: #black at:{location.x, location.y-30,location.z};
			draw shape width:5 color: color;
		}
		else {
			draw shape width:1 color: color;
		}
		//draw link(self,link_db) color: #black;
		//draw "abc" color:#blue size:3;
	}
}


experiment road_traffic type: gui {
	action switch_pressed {
		write rnd(10);
	}
	user_command "switch" action:switch_pressed;
	output {
		//monitor "random name" value:one_of(road).roadname;
		display city_display type:opengl {
			species road aspect: base ;
			species db aspect: view;
			species data_block aspect: view;
			//event " " action: space_pressed;
		}
	}
}
experiment hethong type:gui {
	output {
		display main_display type:opengl {
			species cautruc aspect: sphere3d;
		}
	}
}
