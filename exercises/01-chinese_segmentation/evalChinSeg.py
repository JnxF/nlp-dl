import sys,codecs
from optparse import OptionParser

#handle command line options
parser = OptionParser(usage = """%prog [-v] <segmented_text> <gold_standard>
\nChinese Text Segmentation Evaluation Program
  Compares <segmented_text> to <gold_standard> and outputs the accuracy.
  Files should contain one sentence per line, with words separated by a space.""",version="%prog 0.2")
parser.add_option("-v", "--verbose",action="store_true",dest="verbose",default=False,help="print differing lines to stdout")
(options,args) = parser.parse_args()
if len(args) < 2:
	parser.error("<segmented_text> and <gold_standard> arguments required")

#load file contents
segmented_file = args[0]
with codecs.open(segmented_file,encoding='utf-8') as f:
	seg_text = [line.strip().split() for line in f]
gold_file = args[1]
with codecs.open(gold_file,encoding='utf-8') as f:
	gold_text = [line.strip().split() for line in f]

#sanity checks
# - number of lines must match
seg_text_lines = len(seg_text)
gold_text_lines = len(gold_text)
if seg_text_lines != gold_text_lines:
	sys.stderr.write("Error: Files differ in number of lines:\n  {0}\t= {1}\n  {2}\t= {3}\n".format(segmented_file,seg_text_lines,gold_file,gold_text_lines))
	sys.exit(1)
# - characters on each line (ignoring whitespace) must match
ch_seg = ["".join(s) for s in seg_text]
ch_gold = ["".join(s) for s in gold_text]
if ch_seg != ch_gold:
	mismatches = filter(lambda i:ch_seg[i]!=ch_gold[i],range(len(ch_gold)))
	linenums = ", ".join(str(i+1) for i in mismatches[:100])
	if len(mismatches) > 100:
		linenums += ", ..."
	sys.stderr.write("Error: Files differ by line content (mismatch on lines: {0})\n".format(linenums))
	sys.exit(1)

#calculate accuracy
score = 0
total_words = 0
for i in range(gold_text_lines):
	seg_line = seg_text[i]
	gold_line = gold_text[i]
	total_words += len(gold_line)

	gold_words = set(gold_line)
	line_score = len(filter(gold_words.__contains__,seg_line))
	score += line_score

	if options.verbose and line_score!=len(gold_line):
		sl = " ".join(seg_line).encode("utf8")
		gl = " ".join(gold_line).encode("utf8")
		sc = 100.0*float(line_score)/float(len(gold_line))
		sys.stdout.write("*** Seg: {0}\tGold: {1}\t(line accuracy = {2:.3f}%)\n".format(sl,gl,sc))

sys.stdout.write("Segmentation Accuracy: {0:.3f}%\n".format(100.0*float(score)/float(total_words)))
