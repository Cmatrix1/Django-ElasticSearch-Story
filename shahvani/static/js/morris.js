$(function () {
    "use strict";


	
	// Extra chart
	 Morris.Area({
		element: 'extra-area-chart',
		data: [{
					period: '1394',
					iphone: 0,
					ipad: 0,
					itouch: 0
				}, {
					period: '1395',
					iphone: 50,
					ipad: 15,
					itouch: 5
				}, {
					period: '1396',
					iphone: 20,
					ipad: 50,
					itouch: 65
				}, {
					period: '1397',
					iphone: 60,
					ipad: 12,
					itouch: 7
				}, {
					period: '1398',
					iphone: 30,
					ipad: 20,
					itouch: 120
				}, {
					period: '1399',
					iphone: 25,
					ipad: 80,
					itouch: 40
				}, {
					period: '1400',
					iphone: 10,
					ipad: 10,
					itouch: 10
				}


				],
				lineColors: ['#1dc130', '#2f3d4a', '#009efb'],
				xkey: 'period',
				ykeys: ['iphone', 'ipad', 'itouch'],
				labels: ['وب سایت A', 'وب سایت B', 'وب سایت C'],
				pointSize: 0,
				lineWidth: 0,
				resize:true,
				fillOpacity: 0.8,
				behaveLikeLine: true,
				gridLineColor: '#e0e0e0',
				hideHover: 'auto'
			
		});
}); 