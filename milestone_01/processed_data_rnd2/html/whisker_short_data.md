
<!DOCTYPE html
  PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><body><div class="content"><h2>Contents</h2><div><ul><li><a href="#1">clear all</a></li><li><a href="#2">Unfiltered Whisker Data</a></li></ul></div><h2 id="1">clear all</h2><pre class="codeinput">clc; clear; close <span class="string">all</span>;
</pre><h2 id="2">Unfiltered Whisker Data</h2><pre class="codeinput">relaxed = csvread(<span class="string">"whisker-short-length-relaxed.csv"</span>);
relaxed1 = csvread(<span class="string">"whisker-short-length-relaxed-1.csv"</span>);
relaxed2 = csvread(<span class="string">"whisker-short-length-relaxed-2.csv"</span>);
concave = csvread(<span class="string">"whisker-short-length-concave.csv"</span>);
convex = csvread(<span class="string">"whisker-short-length-convex.csv"</span>);
testData = csvread(<span class="string">"whisker-short-length-test.csv"</span>);
convexTest = csvread(<span class="string">"whisker-short-length-test-convex.csv"</span>);

figure;
hold <span class="string">on</span>;
n = 256;
plot(movmean(relaxed,n))
plot(movmean(relaxed1,n))
plot(movmean(relaxed2,n))
plot(movmean(concave,n))
plot(movmean(convex,n))
plot(movmean(testData,n))
plot(movmean(convexTest,n))
title(<span class="string">"Test Data compared to different measures"</span>)

legend(<span class="string">"relaxed"</span>,<span class="string">"relaxed1"</span>,<span class="string">"relaxed2"</span>,<span class="string">"concave"</span>,<span class="string">"convex"</span>,<span class="string">"testData"</span>,<span class="string">"convexTest"</span>);
</pre><img vspace="5" hspace="5" src="whisker_short_data_01.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2022a</a><br></p></div></body></html>