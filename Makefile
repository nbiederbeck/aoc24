all: 01


%: src/%.py in/%.txt
	python $<


in/%.txt: src/utils.py | in
	python $< $*


in:
	mkdir -p $@


clean:
	rm -rf in out


.PHONY: all clean
