
   <h2>Reading and Writing</h2>
    <div>
        <p>In Rosalind, sample datasets are given as files.&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> has a lot of functions for reading and writing information in files.</p>
        <p>To access a file, you must first open it. To do so, you can use the&nbsp;<code>open()</code> function, which takes two parameters: the name of the target file and the mode. Three modes are available:</p>
        <ul>
            <li><code>r</code> - read mode (the file is opened for reading)</li>
            <li><code>w</code> - write mode (the file is opened for writing, and if a file having the same name exists, it will be erased)</li>
            <li>
                <p><code>a</code> - append mode (the file is opened for appending, which means that data is only to be added to the existing data in the file)</p>
                <div>
                    <pre>f = open(&apos;input.txt&apos;, &apos;r&apos;)</pre>
                </div>
            </li>
        </ul>
        <p>This code told&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> to open the file&nbsp;<code>input.txt</code> in&nbsp;<code>r</code> mode and store the result of this operation in a file object called&nbsp;<code>f</code>.</p>
        <p>To obtain data from the file object you created, you can apply the following methods:</p>
        <p>The command&nbsp;<code>f.read(n)</code> returns&nbsp;<span data-mathml='<math xmlns="http://www.w3.org/1998/Math/MathML"><mi>n</mi></math>' style="display: inline; font-style: normal; font-weight: normal; line-height: normal; font-size: 13px; text-indent: 0px; text-align: left; text-transform: none; letter-spacing: normal; word-spacing: normal; overflow-wrap: normal; white-space: nowrap; float: none; direction: ltr; max-width: none; max-height: none; min-width: 0px; min-height: 0px; border: 0px; padding: 0px; margin: 0px; position: relative;" tabindex="0">nn</span> bytes of data from the file as a string. When the size parameter is omitted, the entire contents of the file will be read and returned.</p>
        <p>The command&nbsp;<code>f.readline()</code> takes a single line from the file. Every line (except the last line of file) terminates in a newline character (<code>\n</code>). To remove this character from the end of a line you have read, use the&nbsp;<code>.strip()</code> method. Note that every time you call&nbsp;<code>.readline()</code> it takes the next line in the file.</p>
        <p>The command&nbsp;<code>f.readlines()</code> returns a list containing every line in the file. If you need to obtain a particular line, you can use a list item index, e.g.,&nbsp;<code>f.readlines()[2]</code> returns the third line of the file object&nbsp;<code>f</code> (don&apos;t forget that&nbsp;<a href="https://rosalind.info/glossary/python/" rel="tooltip">Python</a> utilizes 0-based numbering!)</p>
        <p>An alternative way to read lines is to loop over the file object.</p>
        <div>
            <pre>for line in f:
  print line</pre>
        </div>
        <p>Using this loop, you can do anything you need with every line in the file.</p>
        <p>If the data in the file are not separated by new lines but rather by whitespace, commas, or any other delimeter, then all three commands above will return the data only in the form of lines. As a workaround, you can use the command&nbsp;<code>line.split()</code>. It uses whitespace in addition to&nbsp;<code>\n</code> as delimeters by default, and runs of the same delimiter are regarded as a single separating space. For example,</p>
        <p><code>&apos;Beautiful is better than ugly.\n&apos;.split()</code> returns&nbsp;<code>[&apos;Beautiful&apos;, &apos;is&apos;, &apos;better&apos;, &apos;than&apos;, &apos;ugly.&apos;]</code></p>
        <p>You can even specify the delimiter as a parameter of&nbsp;<code>line.split()</code>:</p>
        <p><code>&apos;Explicit, is better, than implicit.&apos;.split(&quot;,&quot;)</code> returns&nbsp;<code>[&apos;Explicit&apos;, &apos; is better&apos;, &apos; than implicit.&apos;]</code></p>
        <p>Another convenient command for file parsing is&nbsp;<code>.splitlines()</code>. It returns a list of the lines in the string, breaking at line boundaries. Line breaks are not included.</p>
        <p><code>&apos;Simple is\nbetter than\ncomplex.\n&apos;.splitlines()</code> returns&nbsp;<code>[&apos;Simple is&apos;, &apos;better than&apos;, &apos;complex.&apos;]</code></p>
        <p>When you at last complete all your calculations and obtain a result, you need to store it somewhere. To save a file, output the desired file in write mode (if there is no such file, it will be created automatically):</p>
        <div>
            <pre>f = open(&apos;output.txt&apos;, &apos;w&apos;)</pre>
        </div>
        <p>You can then write your data using&nbsp;<code>.write()</code> method.</p>
        <div>
            <pre>f.write(&apos;Any data you want to write into file&apos;)</pre>
        </div>
        <p>The command&nbsp;<code>f.write(string)</code> writes the contents of&nbsp;<code>string</code> to file&nbsp;<code>f</code>. If you want to write something other than a string (an integer say), you must first convert it to a string by using the function&nbsp;<code>str()</code>.</p>
        <div>
            <pre>inscription = [&apos;Rosalind Elsie Franklin &apos;, 1920, 1958]
s = str(inscription)
f.write(s)</pre>
        </div>
        <p>You also can write list items into a file one at a time by using a&nbsp;<code>for</code> loop:</p>
        <div>
            <pre>for i in inscription:
  f.write(str(i) + &apos;\n&apos;)</pre>
        </div>
        <p>Adding&nbsp;<code>\n</code> to&nbsp;<code>str(i)</code> means that every item will start with a new line.</p>
        <p>When you are finished writing file, don&apos;t forget that you must close it using the command&nbsp;<code>f.close()</code>. It&apos;s a good habit to get into.</p>
    </div>

<h2>Problem</h2>
<p>Given:&nbsp;A file containing at most 1000 lines.</p>
<p>Return:&nbsp;A file containing all the even-numbered lines from the original file. Assume 1-based numbering of lines.</p>
<h2>Sample Dataset</h2>
<div>
    <pre>Bravely bold Sir Robin rode forth from Camelot
Yes, brave Sir Robin turned about
He was not afraid to die, O brave Sir Robin
And gallantly he chickened out
He was not at all afraid to be killed in nasty ways
Bravely talking to his feet
Brave, brave, brave, brave Sir Robin
He beat a very brave retreat</pre>
</div>
<h2>Sample Output</h2>
<div>
    <pre>Yes, brave Sir Robin turned about
And gallantly he chickened out
Bravely talking to his feet
He beat a very brave retreat</pre>
</div>
