#include <unistd.h>
#include <sys/syscall.h>
#include <stdio.h>

// Example of use of function syscall to open a shell
// see "man syscall" to better understand the parameters used ...
// Note anyway that this syscall function is wrapper to the system level syscall 
// (see https://github.molgen.mpg.de/git-mirror/glibc/blob/glibc-2.15/sysdeps/unix/sysv/linux/x86_64/syscall.S#L24-L42)
// with its own ABI calling convention ...

char binsh[]="/bin/sh";

int main(){
	long err ;

	// 59 is the number to use in order to call execve 
	// (see for instance https://filippo.io/linux-syscall-table/)
	err = syscall (59, binsh, 0, 0) ; 
	if (err) printf("PB !\n") ;

	return 0 ;
}
