#include <stdio.h>

int main() {
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);

    __auto_type v0 = __builtin_apply_args();
    __auto_type v1 = __builtin_constant_p(v0);  // const 0
    __auto_type v2 = __builtin_isascii(v1);  // const 1

    // alloca future pointers to which we will write, give some extra buffer space for our format string
    __auto_type v500 = __builtin_alloca(v2);
    __auto_type v501 = __builtin_alloca(v2);
    __auto_type v502 = __builtin_alloca(v2);
    __auto_type v503 = __builtin_alloca(v2);
    __auto_type v504 = __builtin_alloca(v2);
    __auto_type v505 = __builtin_alloca(v2);
    __auto_type v506 = __builtin_alloca(v2);
    __auto_type v507 = __builtin_alloca(v2);
    __auto_type v508 = __builtin_alloca(v2);
    __auto_type v509 = __builtin_alloca(v2);
    __auto_type v510 = __builtin_alloca(v2);
    __auto_type v511 = __builtin_alloca(v2);
    __auto_type v512 = __builtin_alloca(v2);
    __auto_type v513 = __builtin_alloca(v2);
    __auto_type v514 = __builtin_alloca(v2);
    __auto_type v515 = __builtin_alloca(v2);
    __auto_type v516 = __builtin_alloca(v2);

    __auto_type v3 = __builtin_alloca(v2);
    __auto_type v4 = __builtin_uaddll_overflow(v2, v1, v3);
    // v3 is now a pointer to buf of len 1

    __auto_type v5 = __builtin_malloc(v2);
    __auto_type v6 = __builtin_uaddll_overflow(v1, v1, v5);

    // Allocate a few more buffers so we don't overwrite things
    __auto_type v7 = __builtin_malloc(v2);
    __auto_type v8 = __builtin_malloc(v2);
    __auto_type v9 = __builtin_malloc(v2);

    // Get chars '%', 'p', and 's' via repeated strcat then strlen
    __auto_type v1001=__builtin_strcat(v5,v3);__auto_type v1002=__builtin_strcat(v5,v3);__auto_type v1003=__builtin_strcat(v5,v3);__auto_type v1004=__builtin_strcat(v5,v3);__auto_type v1005=__builtin_strcat(v5,v3);__auto_type v1006=__builtin_strcat(v5,v3);__auto_type v1007=__builtin_strcat(v5,v3);__auto_type v1008=__builtin_strcat(v5,v3);__auto_type v1009=__builtin_strcat(v5,v3);__auto_type v1010=__builtin_strcat(v5,v3);__auto_type v1011=__builtin_strcat(v5,v3);__auto_type v1012=__builtin_strcat(v5,v3);__auto_type v1013=__builtin_strcat(v5,v3);__auto_type v1014=__builtin_strcat(v5,v3);__auto_type v1015=__builtin_strcat(v5,v3);__auto_type v1016=__builtin_strcat(v5,v3);__auto_type v1017=__builtin_strcat(v5,v3);__auto_type v1018=__builtin_strcat(v5,v3);__auto_type v1019=__builtin_strcat(v5,v3);__auto_type v1020=__builtin_strcat(v5,v3);__auto_type v1021=__builtin_strcat(v5,v3);__auto_type v1022=__builtin_strcat(v5,v3);__auto_type v1023=__builtin_strcat(v5,v3);__auto_type v1024=__builtin_strcat(v5,v3);__auto_type v1025=__builtin_strcat(v5,v3);__auto_type v1026=__builtin_strcat(v5,v3);__auto_type v1027=__builtin_strcat(v5,v3);__auto_type v1028=__builtin_strcat(v5,v3);__auto_type v1029=__builtin_strcat(v5,v3);__auto_type v1030=__builtin_strcat(v5,v3);__auto_type v1031=__builtin_strcat(v5,v3);__auto_type v1032=__builtin_strcat(v5,v3);__auto_type v1033=__builtin_strcat(v5,v3);__auto_type v1034=__builtin_strcat(v5,v3);__auto_type v1035=__builtin_strcat(v5,v3);__auto_type v1036=__builtin_strcat(v5,v3);__auto_type v1037=__builtin_strcat(v5,v3);
    __auto_type v3000 = __builtin_strlen(v5);

    __auto_type v2038=__builtin_strcat(v5,v3);__auto_type v2039=__builtin_strcat(v5,v3);__auto_type v2040=__builtin_strcat(v5,v3);__auto_type v2041=__builtin_strcat(v5,v3);__auto_type v2042=__builtin_strcat(v5,v3);__auto_type v2043=__builtin_strcat(v5,v3);__auto_type v2044=__builtin_strcat(v5,v3);__auto_type v2045=__builtin_strcat(v5,v3);__auto_type v2046=__builtin_strcat(v5,v3);__auto_type v2047=__builtin_strcat(v5,v3);__auto_type v2048=__builtin_strcat(v5,v3);__auto_type v2049=__builtin_strcat(v5,v3);__auto_type v2050=__builtin_strcat(v5,v3);__auto_type v2051=__builtin_strcat(v5,v3);__auto_type v2052=__builtin_strcat(v5,v3);__auto_type v2053=__builtin_strcat(v5,v3);__auto_type v2054=__builtin_strcat(v5,v3);__auto_type v2055=__builtin_strcat(v5,v3);__auto_type v2056=__builtin_strcat(v5,v3);__auto_type v2057=__builtin_strcat(v5,v3);__auto_type v2058=__builtin_strcat(v5,v3);__auto_type v2059=__builtin_strcat(v5,v3);__auto_type v2060=__builtin_strcat(v5,v3);__auto_type v2061=__builtin_strcat(v5,v3);__auto_type v2062=__builtin_strcat(v5,v3);__auto_type v2063=__builtin_strcat(v5,v3);__auto_type v2064=__builtin_strcat(v5,v3);__auto_type v2065=__builtin_strcat(v5,v3);__auto_type v2066=__builtin_strcat(v5,v3);__auto_type v2067=__builtin_strcat(v5,v3);__auto_type v2068=__builtin_strcat(v5,v3);__auto_type v2069=__builtin_strcat(v5,v3);__auto_type v2070=__builtin_strcat(v5,v3);__auto_type v2071=__builtin_strcat(v5,v3);__auto_type v2072=__builtin_strcat(v5,v3);__auto_type v2073=__builtin_strcat(v5,v3);__auto_type v2074=__builtin_strcat(v5,v3);__auto_type v2075=__builtin_strcat(v5,v3);__auto_type v2076=__builtin_strcat(v5,v3);__auto_type v2077=__builtin_strcat(v5,v3);__auto_type v2078=__builtin_strcat(v5,v3);__auto_type v2079=__builtin_strcat(v5,v3);__auto_type v2080=__builtin_strcat(v5,v3);__auto_type v2081=__builtin_strcat(v5,v3);__auto_type v2082=__builtin_strcat(v5,v3);__auto_type v2083=__builtin_strcat(v5,v3);__auto_type v2084=__builtin_strcat(v5,v3);__auto_type v2085=__builtin_strcat(v5,v3);__auto_type v2086=__builtin_strcat(v5,v3);__auto_type v2087=__builtin_strcat(v5,v3);__auto_type v2088=__builtin_strcat(v5,v3);__auto_type v2089=__builtin_strcat(v5,v3);__auto_type v2090=__builtin_strcat(v5,v3);__auto_type v2091=__builtin_strcat(v5,v3);__auto_type v2092=__builtin_strcat(v5,v3);__auto_type v2093=__builtin_strcat(v5,v3);__auto_type v2094=__builtin_strcat(v5,v3);__auto_type v2095=__builtin_strcat(v5,v3);__auto_type v2096=__builtin_strcat(v5,v3);__auto_type v2097=__builtin_strcat(v5,v3);__auto_type v2098=__builtin_strcat(v5,v3);__auto_type v2099=__builtin_strcat(v5,v3);__auto_type v2100=__builtin_strcat(v5,v3);__auto_type v2101=__builtin_strcat(v5,v3);__auto_type v2102=__builtin_strcat(v5,v3);__auto_type v2103=__builtin_strcat(v5,v3);__auto_type v2104=__builtin_strcat(v5,v3);__auto_type v2105=__builtin_strcat(v5,v3);__auto_type v2106=__builtin_strcat(v5,v3);__auto_type v2107=__builtin_strcat(v5,v3);__auto_type v2108=__builtin_strcat(v5,v3);__auto_type v2109=__builtin_strcat(v5,v3);__auto_type v2110=__builtin_strcat(v5,v3);__auto_type v2111=__builtin_strcat(v5,v3);__auto_type v2112=__builtin_strcat(v5,v3);
    __auto_type v3001 = __builtin_strlen(v5);

    __auto_type v2113=__builtin_strcat(v5,v3);__auto_type v2114=__builtin_strcat(v5,v3);__auto_type v2115=__builtin_strcat(v5,v3);
    __auto_type v3002 = __builtin_strlen(v5);

    // Write "%s" to v5 and "%p" to v3102
    __auto_type v3100 = __builtin_malloc(v3002);
    __auto_type v3101 = __builtin_malloc(v3002);
    __auto_type v3102 = __builtin_malloc(v3002);

    __auto_type v3103 = __builtin_uaddll_overflow(v3000, v1, v3100);
    __auto_type v3104 = __builtin_strcpy(v5, v3100);
    __auto_type v3105 = __builtin_uaddll_overflow(v3002, v1, v3100);
    __auto_type v3106 = __builtin_strcat(v5, v3100);

    __auto_type v3200 = __builtin_uaddll_overflow(v3000, v1, v3100);
    __auto_type v3201 = __builtin_strcpy(v3102, v3100);
    __auto_type v3202 = __builtin_uaddll_overflow(v3001, v1, v3100);
    __auto_type v3203 = __builtin_strcat(v3102, v3100);

    // Read input into v3, make this a format string chal
    // Leak stuff
    __auto_type v209 = __builtin_scanf(v5, v3);
    __auto_type v210 = __builtin_printf(v3);

    // Now arb write stuff, take in a pointer and give arb write
__auto_type v300=__builtin_scanf(v3102,v500);__auto_type v301=__builtin_scanf(v5,v3);__auto_type v302=__builtin_printf(v3);__auto_type v303=__builtin_scanf(v3102,v500);__auto_type v304=__builtin_scanf(v5,v3);__auto_type v305=__builtin_printf(v3);__auto_type v306=__builtin_scanf(v3102,v500);__auto_type v307=__builtin_scanf(v5,v3);__auto_type v308=__builtin_printf(v3);__auto_type v309=__builtin_scanf(v3102,v500);__auto_type v310=__builtin_scanf(v5,v3);__auto_type v311=__builtin_printf(v3);__auto_type v312=__builtin_scanf(v3102,v500);__auto_type v313=__builtin_scanf(v5,v3);__auto_type v314=__builtin_printf(v3);__auto_type v315=__builtin_scanf(v3102,v500);__auto_type v316=__builtin_scanf(v5,v3);__auto_type v317=__builtin_printf(v3);__auto_type v318=__builtin_scanf(v3102,v500);__auto_type v319=__builtin_scanf(v5,v3);__auto_type v320=__builtin_printf(v3);__auto_type v321=__builtin_scanf(v3102,v500);__auto_type v322=__builtin_scanf(v5,v3);__auto_type v323=__builtin_printf(v3);__auto_type v324=__builtin_scanf(v3102,v500);__auto_type v325=__builtin_scanf(v5,v3);__auto_type v326=__builtin_printf(v3);__auto_type v327=__builtin_scanf(v3102,v500);__auto_type v328=__builtin_scanf(v5,v3);__auto_type v329=__builtin_printf(v3);__auto_type v330=__builtin_scanf(v3102,v500);__auto_type v331=__builtin_scanf(v5,v3);__auto_type v332=__builtin_printf(v3);__auto_type v333=__builtin_scanf(v3102,v500);__auto_type v334=__builtin_scanf(v5,v3);__auto_type v335=__builtin_printf(v3);__auto_type v336=__builtin_scanf(v3102,v500);__auto_type v337=__builtin_scanf(v5,v3);__auto_type v338=__builtin_printf(v3);__auto_type v339=__builtin_scanf(v3102,v500);__auto_type v340=__builtin_scanf(v5,v3);__auto_type v341=__builtin_printf(v3);__auto_type v342=__builtin_scanf(v3102,v500);__auto_type v343=__builtin_scanf(v5,v3);__auto_type v344=__builtin_printf(v3);__auto_type v345=__builtin_scanf(v3102,v500);__auto_type v346=__builtin_scanf(v5,v3);__auto_type v347=__builtin_printf(v3);__auto_type v348=__builtin_scanf(v3102,v500);__auto_type v349=__builtin_scanf(v5,v3);__auto_type v350=__builtin_printf(v3);__auto_type v351=__builtin_scanf(v3102,v500);__auto_type v352=__builtin_scanf(v5,v3);__auto_type v353=__builtin_printf(v3);__auto_type v354=__builtin_scanf(v3102,v500);__auto_type v355=__builtin_scanf(v5,v3);__auto_type v356=__builtin_printf(v3);__auto_type v357=__builtin_scanf(v3102,v500);__auto_type v358=__builtin_scanf(v5,v3);__auto_type v359=__builtin_printf(v3);__auto_type v360=__builtin_scanf(v3102,v500);__auto_type v361=__builtin_scanf(v5,v3);__auto_type v362=__builtin_printf(v3);__auto_type v363=__builtin_scanf(v3102,v500);__auto_type v364=__builtin_scanf(v5,v3);__auto_type v365=__builtin_printf(v3);__auto_type v366=__builtin_scanf(v3102,v500);__auto_type v367=__builtin_scanf(v5,v3);__auto_type v368=__builtin_printf(v3);__auto_type v369=__builtin_scanf(v3102,v500);__auto_type v370=__builtin_scanf(v5,v3);__auto_type v371=__builtin_printf(v3);__auto_type v372=__builtin_scanf(v3102,v500);__auto_type v373=__builtin_scanf(v5,v3);__auto_type v374=__builtin_printf(v3);__auto_type v375=__builtin_scanf(v3102,v500);__auto_type v376=__builtin_scanf(v5,v3);__auto_type v377=__builtin_printf(v3);__auto_type v378=__builtin_scanf(v3102,v500);__auto_type v379=__builtin_scanf(v5,v3);__auto_type v380=__builtin_printf(v3);__auto_type v381=__builtin_scanf(v3102,v500);__auto_type v382=__builtin_scanf(v5,v3);__auto_type v383=__builtin_printf(v3);__auto_type v384=__builtin_scanf(v3102,v500);__auto_type v385=__builtin_scanf(v5,v3);__auto_type v386=__builtin_printf(v3);__auto_type v387=__builtin_scanf(v3102,v500);__auto_type v388=__builtin_scanf(v5,v3);__auto_type v389=__builtin_printf(v3);__auto_type v390=__builtin_scanf(v3102,v500);__auto_type v391=__builtin_scanf(v5,v3);__auto_type v392=__builtin_printf(v3);__auto_type v393=__builtin_scanf(v3102,v500);__auto_type v394=__builtin_scanf(v5,v3);__auto_type v395=__builtin_printf(v3);

    return 0;
}
