all: $(addprefix out/, $(addsuffix .txt, 01))


out/%.txt: src/%.py in/%.txt | out
	python $<
	cat $@


in/%.txt: utils.py | int
	python $<


out:
	mkdir -p out


in:
	mkdir -p int


clean:
	rm -rf in out


.PHONY: all clean
