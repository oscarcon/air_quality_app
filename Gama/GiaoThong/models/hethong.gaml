/***
* Name: hethong
* Author: huy
* Description: 
* Tags: Tag1, Tag2, TagN
***/

model hethong

/* Insert your model definition here */

species data_block {
	string url;
	rgb color <- #green;
	list<data_block> subs;
	int level;
	action action_open_url {
		color <- #darkblue;
	}
	aspect view {
		draw shape color: color;
		//draw "text" size: 6 color:#darkblue;
	}
	aspect sphere3d {
		int nb_subs <- length(subs);
		shape <- sphere(50);
		draw shape color:color;
	}
}
