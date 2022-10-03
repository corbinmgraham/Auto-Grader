# Auto-Grader

Have you ever noticed how outdated Scantron scanners and forms are?
Or how they are only formatted for one type of assignment?
This ease of grading has led the entire education system to ditch the
ideas of creativity and allowing students to construct new and creative
ideas for an easier way to grade assignments.

The Auto-Grader NLP is the solution to this issue.  Using modern NLP,
and statisitics, it's possible to predict the accuracy of a student's
answer in many forms of assignments.  This will remove the possibility
of bias from the professor or grader of the assignment while also reducing
the time it takes to grade assignments.

## Pipeline

[Assignment] - scan -> [Non-Formatted Image] - image processing model ->
[Plain-Text (from input)] + [Source-Text (from teacher)] - NLP model + 
statistical comparison -> [Outcome (% accuracy in solution)]

## Accuracy

The model will look for keywords provided in source-text and judge
accuracy of the input from the similarity of keywords and the structure
formatting.  If different keywords are used but the structure concludes
the same ideas, it should still be marked for accuracy.

The model will use a variety of heuristics to determine the accuracy of the
inputted assignment.  These will all affect the degree of accuracy.
Key-word-match: If there is a high similarity in key-word accuracy, the solution
has then a higher degree of accuracy.
Conclusive evidence: If there is a high similarity in sentence structure for
conclusive evidence then there is a higher degree of accuracy.

## Formulation

$A$: Accuracy; $I$: Input; $S$: Source;

$A_T(I) = ( A_{Noun+Verbage}(S-I) + A_{Evidence}(S-I) + A_{Length}(S-I) + {Random} ) / T_S$
