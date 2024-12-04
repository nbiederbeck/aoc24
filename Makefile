all: $(addprefix out/, $(addsuffix .txt, 01))


out/%.txt: src/%.py in/%.txt | out
	python $<
	cat $@


in/%.txt: src/utils.py | in
	python $< $*


out:
	mkdir -p $@


in:
	mkdir -p $@


clean:
	rm -rf in out


.PHONY: all clean
