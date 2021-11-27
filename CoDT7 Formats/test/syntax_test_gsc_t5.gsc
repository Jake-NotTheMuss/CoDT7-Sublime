/* SYNTAX TEST "Packages/CoDT7 Formats/GSC.sublime-syntax" */

REGISTER_SYSTEM("test", &__init__, undefined)
/* <- - entity.name */

t5_function(&param, param1)
/* <- meta.function entity.name */
/*         ^ meta.function.parameters */
/*           ^ variable.parameter */
/*                  ^ variable.parameter */
{
/* <- meta.function */
}
/* <- meta.function */