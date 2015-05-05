all: CW_all.txt input.txt jsoncatalog.txt edit_ofre0001.txt edit_ofre0002.txt

CW_all.txt:
	cat $(wildcard edit*.txt) >> CW_all.txt 

input.txt jsoncatalog.txt: CW_all.txt
	python text_cleaning_CW.py

bookworm:
	git clone https://github.com/Bookworm-project/BookwormDB.git bookworm
	$(MAKE) -C bookworm