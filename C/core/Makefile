TARGET = core
BUILD_DIRS=build
CFLAGS=``
LDFLAGS=``
$(shell mkdir -p $(BUILD_DIRS))
INC=-Iinclude

all: ${TARGET}
core: src/main.cpp
	gcc $(INC) $(CFLAGS) $(LDFLAGS) -g -o build/main src/*
clean:
	rm -f ${TARGET}
