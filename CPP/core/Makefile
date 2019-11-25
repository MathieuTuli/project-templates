TARGET = core
BUILD_DIRS=build
CFLAGS=``
LDFLAGS=``
$(shell mkdir -p $(BUILD_DIRS))
INC=-Iinclude

all: ${TARGET}
core: src/main.cpp
	g++ $(INC) $(CFLAGS) $(LDFLAGS) -o build/main src/*
clean:
	rm -f ${TARGET}
