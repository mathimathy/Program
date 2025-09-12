import function as f
try:
	inventory_object, inventory_tool, tool_activate, inventory_equi = f.load()
except:
	inventory_object = {}
	invotory_tool = {
		'knife': 1
	}
	inventory_equi = {}
	tool_activate = 'knife'
craft_item = {
	'titanium ingot': {
		'titanium': 10
	},
	'fiber mesh': {
		'creepvine sample': 2
	},
	'silicon rubber': {
		'creepvine seed cluster': 2
	},
	'glass': {
		'quartz': 2
	},
	'bleach': {
		'salt deposit': 1,
		'common coral sample': 1
	},
	'lubricant': {
		'creepvine seed cluster': 2
	},
	'magnesium': {
		'salt deposit': 3
	},
	'enameled glass': {
		'stalker tooth': 1,
		'glass': 1
	},
	'pasteel ingot': {
		'titanium ingot': 1,
		'lithium': 1
	},
	'synthetic fibers': {
		'benzene': 1,
		'fiber mesh': 1
	},
	'uranium': {
		'uraninite crystal': 3
	},
	'benzene': {
		'blood oil': 3
	},
	'aerogel': {
		'ruby': 1,
		'gel sack': 1
	},
	'polyaniline': {
		'gold': 1,
		'hidrichloric acid': 1
	},
	'copper wire': {
		'copper ore': 2
	},
	'battery': {
		'acid mushroom': 2,
		'copper ore': 1
	},
	'powercell': {
		'battery': 2,
		'silicon rubber': 1
	},
	'computer chip': {
		'table coral sample': 2,
		'silver ore': 1,
		'quartz': 1
	},
	'wiring kit': {
		'silver ore': 2
	},
	'advanced wiring kit': {
		'gold': 2,
		'computer chip': 1
	},
	'reactor rod': {
		'uranium': 1,
		'lead': 1,
		'titanium': 1
	}
}
craft_tool = {
	'scanner': {
		'titanium': 2,
		'battery': 1
	},
	'welder': {
		'magnesium': 1,
		'crash powder': 1,
		'titanium': 1
	},
	'flashlight': {
		'battery': 1,
		'glass': 1
	},
	'survival knife': {
		'titanium': 1,
		'silicon rubber': 1
	},
	'dive reel': {
		'creepvine sample': 5,
		'titanium': 1
	},
	'air bladder': {
		'silicon rubber': 2,
		'airsack': 1
	},
	'flare': {
		'crash powder': 1
	},
	'habitat builder': {
		'computer chip': 1,
		'battery': 1
	},
	'laser cutter': {
		'battery': 1,
		'diamond': 1,
		'titanium': 1
	},
	'statis riffle': {
		'advanced wiring kit': 1,
		'battery': 1,
		'titanium': 1
	},
	'propulsion cannon': {
		'advanced wiring kit': 1,
		'battery': 1,
		'titanium': 1
	},
	'lightstick': {
		'battery': 1,
		'titanium': 1,
		'glass'
	},
	'sea glide': {
		'battery': 1,
		'lubricant': 1,
		'copper wire': 1,
		'titanium': 1
	},
	'mobile vehicle bay': {
		'titanium ingot': 1,
		'lubricant': 1,
		'power cell': 1
	},
	'beacon': {
		'copper wire': 1,
		'titanium': 1
	},
	'current generator': {
		'battery': 1,
		'lubricant': 1,
		'titanium': 1
	},
	'water proof locker': {
		'titanium': 3
	},
	'gravshpere': {
		'battery': 2,
		'battery': 1,
		'copper wire': 1
	}
}
craft_equi = {
	'O2 tank': {
		'titanium': 4,
		'glass': 1
	},
	'fins': {
		'silicon rubber': 2
	},
	'radiation suit': {
		'fiber mesh': 2,
		'lead': 2
	},
	'still suit': {
		'fiber mesh': 2,
		'silver ore': 2
	},
	'first aid kit': {
		'bleach': 1,
		'fiber mesh': 1
	},
	'rebreather': {
		'wiring kit': 1,
		'fiber mesh': 1
	},
	'pipe': {
		'titanium': 3
	},
	'compass': {
		'magnetite': 1,
		'computer chip': 1
	},
	'thermometer': {
		'computer chip': 1
	},
	'high capacity O2 tank': {
		'O2 tank': 1,
		'lithium': 4
	},
	'swim charge fins': {
		'fins': 1,
		'polyaniline': 1,
		'wiring kit': 1
	},
	'ultra-glide fins': {
		'fins': 1,
		'titanium': 1,
		'lithium': 1,
		'silicon rubber': 2
	}
}