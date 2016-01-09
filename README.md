# latex2mathml
Pure Python library for LaTeX to MathML conversion.

## Demo
[latex2mathml Demo](http://latex2mathml-reaqtor.rhcloud.com/)

_\*Tested in Firefox only_


## Examples

### Identifiers, Numbers and Operators

#### LaTeX Input
```latex
x
```

#### MathML Output
```html
<math>
    <mrow>
        <mi>
            x
        </mi>
    </mrow>
</math>
```

#### LaTeX Input
```latex
xyz
```

#### MathML Output
```html
<math>
    <mrow>
        <mi>
            x
        </mi>
        <mi>
            y
        </mi>
        <mi>
            z
        </mi>
    </mrow>
</math>
```

#### LaTeX Input
```latex
3
```

#### MathML Output
```html
<math>
    <mrow>
        <mn>
            3
        </mn>
    </mrow>
</math>
```

#### LaTeX Input
```latex
444
```

#### MathML Output
```html
<math>
    <mrow>
        <mn>
            444
        </mn>
    </mrow>
</math>
```

#### LaTeX Input
```latex
12.34
```

#### MathML Output
```html
<math>
    <mrow>
        <mn>
            12.34
        </mn>
    </mrow>
</math>
```

#### LaTeX Input
```latex
12x
```

#### MathML Output
```html
<math>
    <mrow>
        <mn>
            12
        </mn>
        <mi>
            x
        </mi>
    </mrow>
</math>
```

#### LaTeX Input
```latex
3-2
```

#### MathML Output
```html
<math>
    <mrow>
        <mn>
            3
        </mn>
        <mo>
            &#x02212;
        </mo>
        <mn>
            2
        </mn>
    </mrow>
</math>
```

### Subscripts and Superscripts

#### LaTeX Input
```latex
a_b
```

#### MathML Output
```html
<math>
    <mrow>
        <msub>
            <mi>
                a
            </mi>
            <mi>
                b
            </mi>
        </msub>
    </mrow>
</math>
```

#### LaTeX Input
```latex
a^b
```

#### MathML Output
```html
<math>
    <mrow>
        <msup>
            <mi>
                a
            </mi>
            <mi>
                b
            </mi>
        </msup>
    </mrow>
</math>
```

#### LaTeX Input
```latex
a_b^c
```

#### MathML Output
```html
<math>
    <mrow>
        <msubsup>
            <mi>
                a
            </mi>
            <mi>
                b
            </mi>
            <mi>
                c
            </mi>
        </msubsup>
    </mrow>
</math>
```

### Fractions

#### LaTeX Input
```latex
\frac{1}{2}
```

#### MathML Output
```html
<math>
    <mrow>
        <mfrac>
            <mrow>
                <mn>
                    1
                </mn>
            </mrow>
            <mrow>
                <mn>
                    2
                </mn>
            </mrow>
        </mfrac>
    </mrow>
</math>
```

### Roots

#### LaTeX Input
```latex
\sqrt{2}
```

#### MathML Output
```html
<math>
    <mrow>
        <msqrt>
            <mrow>
                <mn>
                    2
                </mn>
            </mrow>
        </msqrt>
    </mrow>
</math>
```

#### LaTeX Input
```latex
\sqrt[3]{2}
```

#### MathML Output
```html
<math>
    <mrow>
        <mroot>
            <mrow>
                <mn>
                    2
                </mn>
            </mrow>
            <mrow>
                <mn>
                    3
                </mn>
            </mrow>
        </mroot>
    </mrow>
</math>
```

### Matrices

#### LaTeX Input
```latex
\begin{matrix}a & b \\ c & d \end{matrix}
```

#### MathML Output
```html
<math>
    <mrow>
        <mtable>
            <mtr>
                <mtd>
                    <mi>
                        a
                    </mi>
                </mtd>
                <mtd>
                    <mi>
                        b
                    </mi>
                </mtd>
            </mtr>
            <mtr>
                <mtd>
                    <mi>
                        c
                    </mi>
                </mtd>
                <mtd>
                    <mi>
                        d
                    </mi>
                </mtd>
            </mtr>
        </mtable>
    </mrow>
</math>
```

#### LaTeX Input
```latex
\begin{matrix*}[r]a & b \\ c & d \end{matrix*}
```

#### MathML Output
```html
<math>
    <mrow>
        <mtable>
            <mtr>
                <mtd columnalign='right'>
                    <mi>
                        a
                    </mi>
                </mtd>
                <mtd columnalign='right'>
                    <mi>
                        b
                    </mi>
                </mtd>
            </mtr>
            <mtr>
                <mtd columnalign='right'>
                    <mi>
                        c
                    </mi>
                </mtd>
                <mtd columnalign='right'>
                    <mi>
                        d
                    </mi>
                </mtd>
            </mtr>
        </mtable>
    </mrow>
</math>
```

### References
#### LaTeX
* https://en.wikibooks.org/wiki/LaTeX/Mathematics
* http://artofproblemsolving.com/wiki/index.php?title=Main_Page
* http://milde.users.sourceforge.net/LUCR/Math/
* http://www.forkosh.com/mimetextutorial.html

#### MathML
* http://www.xmlmind.com/tutorials/MathML/


### Author
* Ronie Martinez (ronmarti18@gmail.com)
