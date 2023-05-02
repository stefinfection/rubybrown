# Final Report

### Trials and successes
Our final build differed fairly drastically from our initial proposal (which you can see in our Milestone_01 report). 
We originally hoped to use four mecanum wheels with tactile "whisker" sensors. The reason for our changes was due
to a convergence of events. 

From a technical standpoint, we were unable to get a single timer with four channels to generate PWM output signals. 
This was essential for getting all four motors powered and wheels turning. We tried *every single timer combination 
possible, literally.* (Timer 2 with four channels, Timer 3 with four channels, Timer 2 with two channels and Timer 3
with two channels, Timer 2 with Timer 14 and every other simple timer capable of PWM generation.) We are still unsure
of what was our error in this regard, but we did hook up our test pins from each timer to an oscilloscope and were
absolutely not getting a PWM output signal off of the pins. Eventually, we resigned to using the two-wheel backup
rover since we could only get two channels working.

Another challenge we encountered was using the whiskers. We tried multiple high-quality graphite pencils, along with 
a silver conductive pen, on various types of paper. Every time we would get really unpredictable conductance through
the different whiskers. Resigned to not wanting to deal with really complex filtering and technical error, we switched
to IR sensors. 

Finally, from a personal and logistical perspective, we dealt with two team members with full-time demanding positions, 
conflicting schedules, and major illness. With our project heavily involving a physical component, these hurdles
were progress limiters. We all learned quite a lot from this experience, particularly how critical it is for
each team member to have continuous access to necessary shared resources and understand the various technologies 
essential for a project of this scope. Despite the roadblocks, however, we really came together and played to our
respective strengths to showcase a final product representative of our substantial combined effort.