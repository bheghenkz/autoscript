#!/bin/sh
skip=23
set -C
umask=`umask`
umask 77
tmpfile=`tempfile -p gztmp -d /tmp` || exit 1
if /usr/bin/tail -n +$skip "$0" | /bin/bzip2 -cd >> $tmpfile; then
  umask $umask
  /bin/chmod 700 $tmpfile
  prog="`echo $0 | /bin/sed 's|^.*/||'`"
  if /bin/ln -T $tmpfile "/tmp/$prog" 2>/dev/null; then
    trap '/bin/rm -f $tmpfile "/tmp/$prog"; exit $res' 0
    (/bin/sleep 5; /bin/rm -f $tmpfile "/tmp/$prog") 2>/dev/null &
    /tmp/"$prog" ${1+"$@"}; res=$?
  else
    trap '/bin/rm -f $tmpfile; exit $res' 0
    (/bin/sleep 5; /bin/rm -f $tmpfile) 2>/dev/null &
    $tmpfile ${1+"$@"}; res=$?
  fi
else
  echo Cannot decompress $0; exit 1
fi; exit $res
BZh91AY&SYٔ�}  �_�@0}������~����P~� 	E�MM0���4� d�M=��ᡓM244��2242FM d��1�C&�dhi��ddhd&�� ɑ�c��M44���# ����M4�#�RP5=F�h��2=G�z4�(<�����yN��Ir�T�J�R�RUB���4+�������Y$�{:1$=A�82�+�,���c�\c�
3��dP/��@�#��f"�z(�.�N6Rk�ft�&�wp*�5�n@5�<f%#pD��.���l�R��k��x�������83�W�w���U<�-�_�������P�l,}lj�-�.Ku�Yv۬���&&A�=�g���<̑�<<>!��IF��xV>�M4K��v�s}gf&��Y���]z���1����xI�2�O��=����*�i�y\�ͧ�5�t������Y������.y��U`����{k=nr�q��=z(S	��&�
rO��|��Ò�Қ~��"0��J f�����v�柌�J�b�_}T�d|���|�i8̱�h�.6n=rMIG�^ɛ����$��l8a�hi3��,�.�k����k�rƭה0�٧���$����eUm�c��ǴU��pI!�
�@w�\EX�<&�+ڐ##.#���;�T�m�f������&�扻�/�r���v�ɽ8{��S�ʲ����r���4�����~�󙹅�B+������̑�mk7t�ۼ����?gw�so�қy�b��x��/�������t����dn�L��I�6J9m��9�m1����u�ϷWp�f9SB��L�6��iJNdܶx���n��)r`w;%os���ԲҒ�ɖ��D�h��^�)��v^��-
���ȹ�(Ƨp�Nw>MO�Kw����\d�h�|�qq��[&�'Z��?d��73��'\窲Xm^0��f��`h��b�K���U����#T-��2���ɒ�*8_aRQ���0t̂�r9ܦ�.3�vHu�{�+�	�jL�&f�%�#�4���!�rJ�bjN'/y�3f\R�;"�[�jE�)��q��>�a��{}�R�T���H�����H�
2���