## Addressing Modes

### Reading Data

#### Direct Addresses
`LDA  0x0010` - Load the value <u>at</u> address 0x0010 into the accumulator

```python
def read_direct(self, address):
    return = self.memory[address]
```

#### Immediate Addresses
`LDA #0x0010` - Load the value 0x0010 into the accumulator

```python
def read_immediate(self, value):
    return = value
```

#### Indirect Addresses
`LDA @0x0010` - Load the value from the address stored at 0x0010 into the accumulator

```python
def read_indirect(self, address):
    return = self.memory[self.memory[address]]
```

#### Labeled Addresses
`LDA $Name` - Load the value from the address referenced by the label Name into the accumulator

```python

self.namedAddresses = {

    "Name": 0x0010

}

def read_labeled(self, label):
    return = self.memory[self.namedAddresses[label]]
```

### Writing Data

#### Direct Addresses
`STA  0x0010` - Store the value in the accumulator at address 0x0010

```python
def write_direct(self, address, value):
    self.memory[address] = value
```

#### Indirect Addresses
`STA @0x0010` - Store the value in the accumulator at the address stored at 0x0010

```python
def write_indirect(self, address, value):
    self.memory[self.memory[address]] = value
```

#### Labeled Addresses
`STA $Name` - Store the value in the accumulator at the address referenced by the label Name

```python
def write_labeled(self, label, value):
    self.memory[self.namedAddresses[label]] = value
```

### Creating Labels

`DAT Name` - Create a label 'Name' at the current address

```python
def DAT(self, label):
    # Create a label at the current address, save it to ram (self.memory)
```