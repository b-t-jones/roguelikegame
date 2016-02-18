## Rogue-like Game Individual Project - Project Log  
Repository for roguelike game level 3 individual project.



### Week Beginning 15/02/16

##### Progress: 

* Finished and submitted design report 
* Editing existing implementation to allow data structures to take variable characters for heightmap implementation
* Looking into Perlin noise generation techniques in Java and how to integrate into ASCII panel design

##### Meeting with Dr Friedetzky (16/02/16):

* Discussed ways of introducing differential geometry into final implementation
* Looked into current research
* Discussed possibility of gaining expert opinions from within the University

##### Objectives: 

* Contact relevant members of the department to discuss introducing different aspects into the project (graphical/mathematical)
* Continue with Perlin noise 
* Continue with data structure implementation improvements 



### Week Beginning 08/02/16

##### Progress: 
* 11/12 pages of design report first draft complete
* Deadline at end of week (12/02/16)
* Referencing improvements and certain design aspects must be changed due to further research

##### Meeting with Dr Friedetzky (09/01/16):
* Discussed current draft of design report, highlighted areas that needed more discussion

##### Objectives: 
* Finish design report 


### Week Beginning 01/02/16

##### Progress: 
* 5 pages of design report written
* Improved project plan created based upon improved research into Perlin Noise generation 
* Researched software engineering project plans and evaluation methods

##### Meeting with Dr Friedetzky (02/01/16):
* Discussed current draft of design report, highlighted improvements 

##### Objectives: 
* Continue with design report


### Week Beginning 25/01/16

##### Progress: 
* Catching up on other academic work means slower than usual project progress, extension obtained to compensate
* Design report Abstract, Introduction draft written

##### Meeting with Dr Friedetzky (26/01/16):
* Talked about design report aspects 
* Discussed referencing, and Latex options

##### Objectives: 
* Continue with design report 


### Week Beginning 18/01/16

##### Progress:
* Missed week due to personal reasons at home
* Fiddling with preliminary implementation of cellular automata
* Continued with design report research
* Obtained extension for desing report

##### No meeting with Dr Friedetzky, not in Durham.

##### Objectives: 
* Continue with design report


### Week Beginning 14/12/15

##### Progress:
* Limited tangiable progress, focussing on reading and building up extensive resources and papers for design report
* Plan of design report in progress
* Learned LaTeX basics for design report writing

##### No meeting with Dr Friedetzky, email sufficient. 

##### Objectives:
* Continue with design report 

###Week Beginning 7/12/15
##### Progress:
* Decided upon hybridisation method- Perlin noise + Hilbert/Sierpinski curve
* Looked into Escher worlds- interesting but too tangential
* Looked into potential for 3d gradient functions
* Research for Design Report 

##### Meeting with Dr Friedetzky (8/12/15):
* Research progress report
* Discussed design report details 
* Discussed various source types

##### Objectives:
* Continue as planned with design report research - academic papers/journals key


###Week Beginning 30/11/15
##### Progress:
* Started on structure building tutorial on [(Trystan's Blog)](http://trystans.blogspot.co.uk/2011/08/roguelike-tutorial-03-scrolling-through.html)
* Created basic structure for game implementation in Java JFrame window
* Created very basic 2d noise algorithm (to be improved upon), which looks at each cell and has 50/50 probability of being 0 or 1
* Smoothed this out using smoothing technique from cellular automata, whereby each tile checks surrounding tiles and transforms to the tile most common 
* This creates decent but by no means perfect structures to start a cavelike system on
* Took screenshot1 for progress comparisons
* Researched perlin noise

##### Meeting with Dr Friedetzky (1/12/15):
* Discussed ways to improve current smoothing technique
* Some merit in continuing improvement of cellular automata technique
* Discussed procedural maze generation 
* Discussed alternative to Hilbert curves, [("The Sierpinski Curve")](http://www.tgmdev.be/applications/acheron/curves/curvesierpinski.php)
* Project aims -> build a hybrid of methods potentially including Hilbert curves, cellular automata smoothing, perlin/simplex noise, non-deterministic descent functions
* Discussed potentials for Escher worlds (optical perspective tricks), procedural implications on this approach
* Discussed the idea of separate approaches for different methods as different branches with one main focus branch, other smaller idea branches to be explored
* Discussed merits of generation->test->keep/discard vs generating perfect worlds with a perfect algorithm (cost/time/complexity?)
* Recieved links for Natural Simulation tutorial [(Khan Academy)](https://www.khanacademy.org/computing/computer-programming/programming-natural-simulations/programming-randomness/p/challenge-lvy-walker)

##### Objectives:
* Continue improving cellular automata approach 
* Look at ways of hybridising current methods -> Mathematical curve functions with noise, maze generation and cave smoothing
* Look at Khan academy tutorial for interesting results

---

###Week Beginning 23/11/15
##### Progress:
* Researched + learnt about version control- downloaded EGit for Eclipse
* Researched applet creation for related browser game interaction
* Looked at tutorial on building the structure for the implementation [(Trystan's Blog)](http://trystans.blogspot.co.uk/2011/08/roguelike-tutorial-03-scrolling-through.html)
* Learned about data structures 
    - Plan for 2d ascii array for display
    - 2d array of arrays for metadata
* Looked into Cellular automata approach see [here](http://www.roguebasin.com/index.php?title=Cellular_Automata_Method_for_Generating_Random_Cave-Like_Levels)
    - Has merits and disadvantages
    - Produces interesting cavelike structures
    - Can produce disconnected graphs, too open structures
* Plans for using noise algorithms with some computational physics in differential height and deterministic and non deterministic gradient descent algorithms 

##### Meeting with Dr Friedetzky (24/11/15):
* Discussed plans for progression
* Advice to work on deterministic methods first and then perturbing them with random approaches
* Look more into Hilbert Curves + Noise algorithm/ cellular automata hybrid
* For an extended objective, look at 3d noise approach and smooth out with a gradient descent algorithm for pathfinding through the route

##### Objectives: 
* Continue to investigate algorithmic options as discussed in meeting
* Continue to develop implementation -> try simple approaches for noise algorithms, cellular automata, Hilbert curves by Christmas 


---

### Week Beginning 16/11/15
##### Progress:
* Learned markdown language for project log on GitHub repository
* Read through related work titles sent by Dr Friedetzky
* Set up online project log
* Currently looking into polygonal map generation demo still

##### Meeting with Dr Friedetzky (18/11/15):
* Discussed Nethack and alternatives like ADOM and Anglan wrt world building approaches
* Discussed possibility of hexagonal grids + associated challenges
* Discussed fractal approaches
* Discussed merits of using hybrid approaches for world building to produce interesting results

##### Objectives:
* Mostly research based this week- come up with new ideas for algorithmic approaches
* Look at hybridisation of ideas
* Make a start on implementation structure (including set up of Eclipse/ IDE)

---

### Week Beginning 9/11/15
##### Progress:
* Converted project plan to Latex
* Research resulted in finding a good demonstration into [polygonal map generation](http://www-cs-students.stanford.edu/~amitp/game-programming/polygon-map-generation/)
* Learned finer details of GitHub repositories and now have a workable cloned directory

##### Meeting with Dr Friedetzky (10/11/15):
###### Discussion points:
* Note importance of data structures
    - Important implementation details now have big effects on end project
    - Potential to experiment with a few to see outcomes
    - Possibility for nested 2d arrays?
* Discussed looking into polygonal generation demo and creating a similar result in Java
* Discussed possibility of reading into related work

##### Objectives:
* Aim to have a working demo of the polygonal generation to get an idea and feel for data structures and algorithmic techniques
* Read design report and project plans from related work
* Continue with producing online project log (maybe in form of a blog?)

---

### Week Beginning 2/11/15
##### Progress:
* Progress includes the creation of GitHub repository to store code and to have an online record of work (this project log). 
* Attended University skills session workshop for introduction to Latex
* Completed project plan
* Plan to begin recording meetings with Dr Friedetzky formally each week for project log

##### Meeting with Dr Friedetzky (04/11/15):
###### Discussion points:
* Log book clarification
* Project plan amendments
* Discussed design report
    - Early implementation stages
    - How I envision it all to work together
    - Agile/waterfall construction?
    - How the work will be done
    - How will the work be tested/evaluated?

##### Objectives:
* Continue to learn Latex
* Create project log
* Research some more algorithmic techniques

---

### Week Beginning 26/10/15
 Progress includes all research over summer into different algorithms and implementation details.

#####  Meeting with Dr Friedetzky (27/10/15):
###### Discussion points:
* Discussed implementation details & use of libraries
    - Focus is on algorithmic quality, not UI
    - With that in mind, 2D ascii is the likely choice
    - Other alternatives explored include unity, Dart
    - To be explored further: Jframe, Libjsci
* Discussed lack of scientific literature
    - Some of the best resources come from informal sources\casual programmers\blogs
    - These can be used but validity needs to be recognised
* Discussed the idea of multiple focuses
    - It's okay to have more than one focus
    - Experimental work on related outside topics is encouraged, even if outcome is infeasible/unhelpful
* Discussed reproducible seeding
    - Decided to proceed with reproducible seeding
* Discussed the topic of puzzle research
    - Might be fruitless but worth looking into
    - Potential to edit deliverables
 
##### Objectives for next week:
* Look into ways of formalising and recording ideas
* Improve recording process
* Look at GitHub or similar
* Look into use of Latex for report writing
* Draft Project Plan


