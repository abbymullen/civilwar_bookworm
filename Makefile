all: edit_ofre0001.txt edit_ofre0002.txt edit_ofre0003.txt edit_ofre0004.txt edit_ofre0005.txt edit_ofre0006.txt edit_ofre0007.txt edit_ofre0008.txt edit_ofre0009.txt edit_ofre0010.txt edit_ofre0011.txt edit_ofre0012.txt edit_ofre0013.txt edit_ofre0014.txt edit_ofre0015.txt edit_ofre0016.txt edit_ofre0017.txt edit_ofre0018.txt edit_ofre0019.txt edit_ofre0020.txt edit_ofre0021.txt edit_ofre0022.txt edit_ofre0023.txt edit_ofre0024.txt edit_ofre0025.txt edit_ofre0026.txt edit_ofre0027.txt CW_all.txt input.txt jsoncatalog.txt

ofre%.txt:
	curl -O http://ebooks.library.cornell.edu/m/moawar/text/$@

CW_all.txt:
	cat $(wildcard edit*.txt) >> CW_all.txt 

input.txt jsoncatalog.txt:CW_all.txt
	python text_cleaning_CW.py

bookworm: input.txt jsoncatalog.txt
	git clone https://github.com/Bookworm-project/BookwormDB.git bookworm
	$(MAKE) -C bookworm


# These substitutions trim front- and end-matter

edit_ofre0001.txt:ofre0002.txt
	sed -n 661,51178p ofre0001.txt > edit_ofre0001.txt

edit_ofre0002.txt:ofre0002.txt
	sed -n 1260,52011p ofre0002.txt > edit_ofre0002.txt

edit_ofre0003.txt:ofre0003.txt
	sed -n 1351,53747p ofre0003.txt > edit_ofre0003.txt

edit_ofre0004.txt:ofre0004.txt
	sed -n 957,48530p ofre0004.txt > edit_ofre0004.txt

edit_ofre0005.txt:ofre0005.txt
	sed -n 1293,51291p ofre0005.txt > edit_ofre0005.txt
 
edit_ofre0006.txt:ofre0006.txt
	sed -n 1077,49753p ofre0006.txt > edit_ofre0006.txt

edit_ofre0007.txt:ofre0007.txt
	sed -n 1283,51514p ofre0007.txt > edit_ofre0007.txt

edit_ofre0008.txt:ofre0008.txt
	sed -n 1720,56087p ofre0008.txt > edit_ofre0008.txt

edit_ofre0009.txt:ofre0009.txt
	sed -n 1598,52311p ofre0009.txt > edit_ofre0009.txt

edit_ofre0010.txt:ofre0010.txt
	sed -n 1767,52137p ofre0010.txt > edit_ofre0010.txt

edit_ofre0011.txt:ofre0011.txt
	sed -n 1704,54189p ofre0011.txt > edit_ofre0011.txt

edit_ofre0012.txt:ofre0012.txt
	sed -n 2132,56723p ofre0012.txt > edit_ofre0012.txt

edit_ofre0013.txt:ofre0013.txt
	sed -n 1415,49742p ofre0013.txt > edit_ofre0013.txt

edit_ofre0014.txt:ofre0014.txt
	sed -n 1177,47629p ofre0014.txt > edit_ofre0014.txt

edit_ofre0015.txt:ofre0015.txt
	sed -n 1470,44917p ofre0015.txt > edit_ofre0015.txt

edit_ofre0016.txt:ofre0016.txt
	sed -n 2186,57660p ofre0016.txt > edit_ofre0016.txt

edit_ofre0017.txt:ofre0017.txt
	sed -n 1737,56713p ofre0017.txt > edit_ofre0017.txt

edit_ofre0018.txt:ofre0018.txt
	sed -n 1366,52697p ofre0018.txt > edit_ofre0018.txt

edit_ofre0019.txt:ofre0019.txt
	sed -n 1214,51760p ofre0019.txt > edit_ofre0019.txt

edit_ofre0020.txt:ofre0020.txt
	sed -n 1255,52380p ofre0020.txt > edit_ofre0020.txt

edit_ofre0021.txt:ofre0021.txt
	sed -n 1292,56648p ofre0021.txt > edit_ofre0021.txt

edit_ofre0022.txt:ofre0022.txt
	sed -n 1391,54391p ofre0022.txt > edit_ofre0022.txt

edit_ofre0023.txt:ofre0023.txt
	sed -n 1015,43442p ofre0023.txt > edit_ofre0023.txt

edit_ofre0024.txt:ofre0024.txt
	sed -n 984,44180p ofre0024.txt > edit_ofre0024.txt

edit_ofre0025.txt:ofre0025.txt
	sed -n 1199,50251p ofre0025.txt > edit_ofre0025.txt

edit_ofre0026.txt:ofre0026.txt
	sed -n 1163,49884p ofre0026.txt > edit_ofre0026.txt

edit_ofre0027.txt:ofre0027.txt
	sed -n 1496,46328p ofre0027.txt > edit_ofre0027.txt

