
<!DOCTYPE html
  PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><body><div class="content"><h2>Contents</h2><div><ul><li><a href="#1">clear all</a></li><li><a href="#2">Unfiltered Whisker Data</a></li><li><a href="#3">Unfiltered Whisker Data Statistics</a></li><li><a href="#4">Filtered Whisker Data - Geometric Filter</a></li><li><a href="#5">Filtered Whisker Data - Moving Mean</a></li><li><a href="#6">Geometric - Moving Mean comparison</a></li><li><a href="#7">Filtered Whisker Data - Computationally-Cheap</a></li></ul></div><h2 id="1">clear all</h2><pre class="codeinput">clc; clear; close <span class="string">all</span>;
</pre><h2 id="2">Unfiltered Whisker Data</h2><pre class="codeinput">whisker_relaxed = csvread(<span class="string">"relaxed.csv"</span>);
whisker_concave = csvread(<span class="string">"bent-concave.csv"</span>);
whisker_convex = csvread(<span class="string">"bent-convex.csv"</span>);


figure
hold <span class="string">on</span>;
plot(whisker_relaxed)
plot(whisker_concave)
plot(whisker_convex)
title(<span class="string">"Whiskers performance"</span>)

legend(<span class="string">"relaxed"</span>,<span class="string">"concave"</span>,<span class="string">"convex"</span>,<span class="string">"Location"</span>,<span class="string">"southoutside"</span>)
</pre><img vspace="5" hspace="5" src="whisker_data_01.png" alt=""> <h2 id="3">Unfiltered Whisker Data Statistics</h2><pre class="codeinput">figure
hold <span class="string">on</span>;


relaxedMean = mean(whisker_relaxed);
relaxedStd = std(whisker_relaxed);
concaveMean = mean(whisker_concave);
concaveStd = std(whisker_concave);
convexMean = mean(whisker_convex);
convexStd = std(whisker_convex);

subplot(3,1,1)
histogram(whisker_relaxed)
title(<span class="string">"Relaxed Whisker Measurement Distribution"</span>)
subplot(3,1,2)
histogram(whisker_concave)
title(<span class="string">"Concave Whisker Measurement Distribution"</span>)
subplot(3,1,3)
histogram(whisker_convex)
title(<span class="string">"Convex Whisker Measurement Distribution"</span>)

disp(<span class="string">"Unfiltered Whisker Data Statistics:"</span>)
disp(<span class="string">"relaxed whisker:"</span>)
disp(strcat(<span class="string">"  mean: "</span>,string(relaxedMean),<span class="string">"   std: "</span>, string(relaxedStd)))
disp(<span class="string">"relaxed concave bend:"</span>)
disp(strcat(<span class="string">"  mean: "</span>,string(concaveMean),<span class="string">"   std: "</span>, string(concaveStd)))
disp(<span class="string">"relaxed convex bend:"</span>)
disp(strcat(<span class="string">"  mean: "</span>,string(convexMean),<span class="string">"   std: "</span>, string(convexStd)))

disp(<span class="string">"Given that std(mean(samples)) = 1/sqrt(nSamples)*std(samples), we can differentiate the systems with 97% accuracy with the following sample counts:"</span>)

zScoreGoal = 2; <span class="comment">% this gets a bit better than 97% (assuming ideal gaussian filters)</span>
concaveSamples = (zScoreGoal * concaveStd / (concaveMean - relaxedMean))^2; <span class="comment">% concave &amp; relaxed have the closest means</span>
disp(strcat(<span class="string">"  min(concave samples): "</span>,string(concaveSamples)))
</pre><pre class="codeoutput">Unfiltered Whisker Data Statistics:
relaxed whisker:
  mean: 110.8195   std: 0.9641
relaxed concave bend:
  mean: 111.0114   std: 0.98412
relaxed convex bend:
  mean: 110.2471   std: 0.97506
Given that std(mean(samples)) = 1/sqrt(nSamples)*std(samples), we can differentiate the systems with 97% accuracy with the following sample counts:
  min(concave samples): 105.1457
</pre><img vspace="5" hspace="5" src="whisker_data_02.png" alt=""> <h2 id="4">Filtered Whisker Data - Geometric Filter</h2><pre>- First round of samples; simplest filter I could think of</pre><pre class="codeinput">figure
hold <span class="string">on</span>;
n = [128,256,512,1024];
title(<span class="string">"Geometrically-Filtered Whisker Data Output"</span>)
<span class="keyword">for</span> i = 1:length(n)
  subplot(3,2,i)
  hold <span class="string">on</span>;
  plot(lowPassFilter(whisker_relaxed,n(i)))
  plot(lowPassFilter(whisker_concave,n(i)))
  plot(lowPassFilter(whisker_convex,n(i)))
  title(strcat(<span class="string">"n = "</span>,string(n(i))))
<span class="keyword">end</span>
legend(<span class="string">"relaxed"</span>,<span class="string">"concave"</span>,<span class="string">"convex"</span>,<span class="string">"Location"</span>,<span class="string">"southoutside"</span>)

relaxedGeometricError = zeros([1 length(n)]);
concaveGeometricError = zeros([1 length(n)]);
convexGeometricError  = zeros([1 length(n)]);
relaxedConcaveLine = mean([relaxedMean concaveMean]); <span class="comment">% Assuming nearly-equal std</span>
relaxedConvexLine  = mean([relaxedMean convexMean ]); <span class="comment">% Assuming nearly-equal std</span>
<span class="keyword">for</span> i = 1:length(n)
  relaxedWhiskerMean = lowPassFilter(whisker_relaxed,n(i));
  concaveWhiskerMean = lowPassFilter(whisker_concave,n(i));
  convexWhiskerMean  = lowPassFilter(whisker_convex,n(i));
  relaxedGeometricError(i) = getBayesianError(relaxedWhiskerMean,relaxedConvexLine,relaxedConcaveLine);
  concaveGeometricError(i) = getBayesianError(concaveWhiskerMean,relaxedConcaveLine,256);
  convexGeometricError(i)  = getBayesianError(convexWhiskerMean,0,relaxedConcaveLine);
<span class="keyword">end</span>

figure
hold <span class="string">on</span>;
title(<span class="string">"Geometric Filtered Whisker Data Output Error"</span>)
plot(n,relaxedGeometricError);
plot(n,concaveGeometricError);
plot(n,convexGeometricError);
legend(<span class="string">"Relaxed Whisker Error"</span>,<span class="string">"Concave Whisker Error"</span>,<span class="string">"Convex Whisker Error"</span>);
</pre><img vspace="5" hspace="5" src="whisker_data_03.png" alt=""> <img vspace="5" hspace="5" src="whisker_data_04.png" alt=""> <h2 id="5">Filtered Whisker Data - Moving Mean</h2><p>this can be implemented fairly easily w/ an array of size n.  sum -= array.pop() - newData;  array.plop(newData);</p><pre class="codeinput">figure
hold <span class="string">on</span>;
n = [128,256,512,1024];
title(<span class="string">"Moving Mean Filtered Whisker Data Output"</span>)
<span class="keyword">for</span> i = 1:length(n)
  subplot(2,2,i)
  hold <span class="string">on</span>;
  plot(movmean(whisker_relaxed,n(i)))
  plot(movmean(whisker_concave,n(i)))
  plot(movmean(whisker_convex,n(i)))
  title(strcat(<span class="string">"n = "</span>,string(n(i))))
<span class="keyword">end</span>
legend(<span class="string">"relaxed"</span>,<span class="string">"concave"</span>,<span class="string">"convex"</span>,<span class="string">"Location"</span>,<span class="string">"southeast"</span>)

relaxedMovingMeanError = zeros([1 length(n)]);
concaveMovingMeanError = zeros([1 length(n)]);
convexMovingMeanError  = zeros([1 length(n)]);
relaxedConcaveLine = mean([relaxedMean concaveMean]); <span class="comment">% Assuming nearly-equal std</span>
relaxedConvexLine  = mean([relaxedMean convexMean ]); <span class="comment">% Assuming nearly-equal std</span>
<span class="keyword">for</span> i = 1:length(n)
  relaxedWhiskerMean = movmean(whisker_relaxed,n(i));
  concaveWhiskerMean = movmean(whisker_concave,n(i));
  convexWhiskerMean  = movmean(whisker_convex,n(i));
  relaxedMovingMeanError(i) = getBayesianError(relaxedWhiskerMean,relaxedConvexLine,relaxedConcaveLine);
  concaveMovingMeanError(i) = getBayesianError(concaveWhiskerMean,relaxedConcaveLine,256);
  convexMovingMeanError(i)  = getBayesianError(convexWhiskerMean,0,relaxedConcaveLine);
<span class="keyword">end</span>

figure
hold <span class="string">on</span>;
title(<span class="string">"Moving Mean Filtered Whisker Data Output Error"</span>)
plot(n,relaxedMovingMeanError);
plot(n,concaveMovingMeanError);
plot(n,convexMovingMeanError);
legend(<span class="string">"Relaxed Whisker Error"</span>,<span class="string">"Concave Whisker Error"</span>,<span class="string">"Convex Whisker Error"</span>);
</pre><img vspace="5" hspace="5" src="whisker_data_05.png" alt=""> <img vspace="5" hspace="5" src="whisker_data_06.png" alt=""> <h2 id="6">Geometric - Moving Mean comparison</h2><pre class="codeinput">n = [128,256,512,1024];

figure;
title(<span class="string">"Geometric vs Moving Mean Error Comparison"</span>)
subplot(1,2,1)
hold <span class="string">on</span>
plot(n, relaxedMovingMeanError);
plot(n, relaxedGeometricError);
legend(<span class="string">"Moving Mean Error"</span>, <span class="string">"Geometric Error"</span>)

subplot(1,2,2)
hold <span class="string">on</span>
plot(n, concaveMovingMeanError);
plot(n, concaveGeometricError);
legend(<span class="string">"Moving Mean Error"</span>, <span class="string">"Geometric Error"</span>)

disp(<span class="string">"It seems like a moving mean is a better filter than a geometric filter"</span>)
</pre><pre class="codeoutput">It seems like a moving mean is a better filter than a geometric filter
</pre><img vspace="5" hspace="5" src="whisker_data_07.png" alt=""> <h2 id="7">Filtered Whisker Data - Computationally-Cheap</h2><pre>- Since multiplication/division is expensive, divide by power of two (bit shift)</pre><pre class="codeinput">figure
hold <span class="string">on</span>;
n = [5,7,8,9];
title(<span class="string">"Quick-Filtered Whisker Data Output"</span>)
<span class="keyword">for</span> i = 1:length(n)
  subplot(3,2,i)
  hold <span class="string">on</span>;
  plot(quickFilter(whisker_relaxed,n(i)))
  plot(quickFilter(whisker_concave,n(i)))
  plot(quickFilter(whisker_convex,n(i)))
  title(strcat(<span class="string">"n = "</span>,string(n(i))))
<span class="keyword">end</span>
legend(<span class="string">"relaxed"</span>,<span class="string">"concave"</span>,<span class="string">"convex"</span>,<span class="string">"Location"</span>,<span class="string">"southeast"</span>)
</pre><img vspace="5" hspace="5" src="whisker_data_08.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2022a</a><br></p></div>
</body></html>