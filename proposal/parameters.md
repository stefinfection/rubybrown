# Parameters
The Final Project will produce a vehicle capable of solving the following problem set:
- Obstacle Course
- Drag Race

## Obstacle Course
The obstacle course has been given the following constraints, which invoke their associated questions.
- The Rover will navigate through an obstacle course.
  - Course length & width will be given the day of the rally.
  - *Where will the course be located?*
    - Either in the classroom or in the social area/lobby of the MEB.
      - *When will we know the location?*
        - **We expect to know the definitive location at least 3 weeks prior to the rally.**
  - *What will be the lighting conditions of the course?*
    - **We will be prepared to specify the expected lighting conditions by March 17th**
    - *When will we know them?*
      - **We will need to know the definitive lighting condition & its variance at least 3 weeks prior to the rally.**
- The Obstacle course will be bounded by walls on each side.
  - *What material will the walls be made out of? What tolerance will there be in the direction pointed?*
- The Rover will start at some random position along the starting line.
  - *What direction will the Rover be pointed?*
    - **The Rover will need to be pointed within a 5% slope of parallel to its *nearest* wall.**
  - *Where will vehicle be placed in relation to the starting line?*
    - **We expect the vehicle to be placed as near to the starting line as possible while still placing the vehicle inside the boundary constraints of the obstacle course.**
      - **i.e.: We will design the rover expecting it to only cross the end line.**
- *How will the Start & End lines be delineated?*
  - **If undetermined, we will use [sports floor-marking vinyl tape](https://a.co/d/b2FTbvO) to delineate start & end lines**. 
    - **We will need to know the definitive boundary delineators at least 3 weeks prior to the rally.**
  - **The boundary delineators are expected to be continuous, and completely enclose the space.**
  - *How will the Rover be expected to react to detection of the end delineator?*
- The course will be scattered with unweighted cardboard boxes of various sizes. Movement of cardboard boxes will be penalized.
  - *Will there be dead ends?*
  - *What percentage of the floor space will be covered by obstructions?*
  - *Will there be **any** obstacles other than the cardboard boxes?*
  - **Air conditioning & heating are expected to be disabled.**
  - **No novel material will be placed with the intent of interrupting the wheels' contact with the floor.**
- The rover will have two chances to run the course.
- Only serial access to the rover is allowed; no visual observation will be permitted.
- Score will be a function of:
  - the time required to traverse from start to finish.
  - penalties awarded for violation of stationary box etiquette.

## Drag Race
- Rover will have an unobstructed straight path.
  - *How many rovers will be drag racing simultaneously?*
  - *What will be the lighting conditions of the course?*
    - **We will be prepared to specify the expected lighting conditions by March 17th**
    - *When will we know them?*
      - **We will need to know the definitive lighting condition & its variance at least 3 weeks prior to the rally.**
  - *What direction will the Rover be pointed?*
    - **The Rover will need to be pointed within a 2% slope of parallel to its intended direction of travel.**
  - **The Drag Race is expected to be a second event, *not* the second leg to the obstacle course.**
- Course length will be given day of rally.
  - *How will start and end markers be delineated?*
    - **If undetermined, we will use [sports floor-marking vinyl tape](https://a.co/d/b2FTbvO) to delineate start & end lines**. 
    - **We will need to know the definitive boundary delineators at least 3 weeks prior to the rally.**
    - **The boundary delineators are expected to be continuous, and completely enclose the space.**
  - *Can the rover reverse to correct having gone too far?*
  - *Where will vehicle be placed in relation to the starting line?*
    - **We expect the vehicle to be placed as near to the starting line as possible while still placing the vehicle inside the boundary constraints of the drag course.**
      - **i.e.: We will design the rover expecting it to only cross (and stop on) the end line.**
- Score will be a function of:
  - Time taken to traverse the length of the course.
  - Distance from the finish line (measured from the center point of the rover)
