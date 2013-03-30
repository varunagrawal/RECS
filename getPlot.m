function getPlot(x)
	mu = mean(x);
	sigma = std(x);
	fx = (1/sqrt(2*pi*sigma^2)*exp(-(x-mu).^2/(2*sigma^2)));
	
	plot(x, zeros(size(x)(1)), '+', "markersize", 15);
	hold on;
	plot(x, fx, 'r', "markersize", 15);
	
	axis([-10000 100000 -0.00001 0.00005]);
	xlabel('Rank');	
	hold off;

endfunction;
