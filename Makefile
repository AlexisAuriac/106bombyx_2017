##
## EPITECH PROJECT, 2017
## 106bombyx
## File description:
## Makefile for 106bombyx
##

NAME	=	106bombyx

all	:	$(NAME)

$(NAME)	:
		cp bombyx.py 106bombyx

fclean	:
		rm -f $(NAME)

re	:	fclean	all

.PHONY	:	all fclean re
