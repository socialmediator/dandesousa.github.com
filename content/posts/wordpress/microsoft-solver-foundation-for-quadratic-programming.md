Title: Microsoft Solver Foundation for Quadratic Programming
Date: 2010-07-15 21:55
Author: Admin
Category: Programming
Tags: .net, C#, math

The Microsoft Solver Foundation provides some excellent APIs for solving
optimization problems in C\# .NET. Getting to documentation about the
Quadratic Programming facilities can be a bit tricky though. I've added
below some sample code to help out with this.

In the following example I'm solving an example of the lagrangian dual
form used for classification in an SVM.

    :::csharp
    InteriorPointSolver solver = new InteriorPointSolver();
    // Langrangian Dual
    int dual = 0;
    solver.AddRow("L", out dual);
    // Sum Constraint
    int linearConstraint = 0;
    solver.AddRow("SumConstraint", out linearConstraint);
    // Add variables and Lagrangian linear terms
    int[] vars = new int[n];
    for (int i = 0; i &lt; n; i++)
    {
        // Add the variable
        solver.AddVariable("a" + i, out vars[i]);
        // Factor in C upper bounds
        solver.SetBounds(vars[i], 0, C);
    }
    // Linear constraint must equal 0
    solver.SetBounds(linearConstraint, 0, 0);
    // Lagrangian Quadratic Terms
    for (int i = 0; i &lt; n; i++) { solver.SetCoefficient(linearConstraint,
            vars[i], trainingData[i].output()); solver.SetCoefficient(dual, vars[i],
            1); Parallel.For(0, n, o, (int j) =&gt;
                {
                double coef = trainingData[i].output() \* trainingData[j].output() \*
                kernel.evaluate(trainingData[i].point(), trainingData[j].point());
                solver.SetCoefficient(dual, -0.5 \* coef, vars[i], vars[j]);
                });
    }
    solver.AddGoal(dual, 0, false);
    InteriorPointSolverParams param = new
    InteriorPointSolverParams();[/csharp]

Essentially all we are doing here is adding all the variables to our
constraint optimization problem and asking the solver to minimize. The
vars array simply expressing a list of identifier for variables in the
constraint problem. You should fire up the Solver Foundation library and
give it a shot yourself.

Here are some resources that should make understanding this a bit easier
as well. Its the official blog of one of the key developers on the
project, specifically the links to tutorial on the quadratic programming
solver.

[Nathan Brixius' QP Solver Tutorial][]

  [Nathan Brixius' QP Solver Tutorial]: http://blogs.msdn.com/b/natbr/archive/2009/09/24/using-the-solver-foundation-interior-point-solver.aspx
