
<!DOCTYPE html
  PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN">
<html><body><div class="content"><h2>Contents</h2><div><ul><li><a href="#1">clear all</a></li><li><a href="#2">Photo Resistor data</a></li></ul></div><h2 id="1">clear all</h2><pre class="codeinput">clc; clear; close <span class="string">all</span>;
</pre><h2 id="2">Photo Resistor data</h2><pre class="codeinput">phores_ambiance = csvread(<span class="string">"phores-ambiance.csv"</span>);
phores_blocked = csvread(<span class="string">"phores-blocked.csv"</span>);
phores_white = csvread(<span class="string">"phores-white-paper.csv"</span>);

figure
hold <span class="string">on</span>;
plot(phores_ambiance)
plot(phores_blocked)
plot(phores_white)
title(<span class="string">"photoresistor performance"</span>)

legend(<span class="string">"ambiance"</span>,<span class="string">"blocked"</span>,<span class="string">"white"</span>)

disp(<span class="string">"These data are much cleaner &amp; thusly don't need as much analysis as the whisker_data."</span>)
</pre><pre class="codeoutput">These data are much cleaner &amp; thusly don't need as much analysis as the whisker_data.
</pre><img vspace="5" hspace="5" src="photo_resistor_data_01.png" alt=""> <p class="footer"><br><a href="https://www.mathworks.com/products/matlab/">Published with MATLAB&reg; R2022a</a><br></p></div>
</body></html>