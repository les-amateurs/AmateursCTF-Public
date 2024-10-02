#define RESET   "\033[0m"
#define BLUE    "\033[34m"
#define CYAN    "\033[36m"
#define GREEN   "\033[32m"
#define MAGENTA "\033[95m"
#define RED     "\033[91m"
#define WHITE   "\033[38;2;255;255;255m"
#define YELLOW  "\033[33m"
#define colorify(text, color) color text RESET

#define    blue(text) colorify(text, BLUE)
#define    cyan(text) colorify(text, CYAN)
#define   green(text) colorify(text, GREEN)
#define magenta(text) colorify(text, MAGENTA)
#define     red(text) colorify(text, RED)
#define   white(text) colorify(text, WHITE)
#define  yellow(text) colorify(text, YELLOW)