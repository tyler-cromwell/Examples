#include <linux/kernel.h>
#include <linux/module.h>


/* Module Information */
MODULE_AUTHOR("Tyler Cromwell <tjc6185@gmail.com>");
MODULE_LICENSE("GPL");
MODULE_DESCRIPTION("Example of a basic Linux kernel module");


static int __init begin_module(void) {
    printk(KERN_DEBUG "helloworld: Hello world!\n");
    return 0;
}


static void __exit end_module(void) {
    printk(KERN_DEBUG "helloworld: Goodbye, cruel world.\n");
}


module_init(begin_module);  /* insmod */
module_exit(end_module);    /* rmmod */
