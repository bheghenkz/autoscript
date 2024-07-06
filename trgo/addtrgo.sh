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
BZh91AY&SY^�.  ���L0 ����������P��Z:�����F@�d 4��    ?T��i���h�@� �F�   ��F����2 �=@  2 � � pd4�LCMA�a@h��h  J&�I������&��<SL�4	6��h�Q���TɌ��c�'�2/
��x�O&Ē	�i<�@�"�9W�QP�Da%�IC��o}q\�����`�`��C�{	T��PU|P�t|�h��g7�'��B�A�����=��1�]S#������7	_�2��|;a��O�{.��\ųy�?8E���D�JC@�`�A!ZV�e���C�����<T�77DDT(�p�ŨE�����fJ�L4��!"�� ӅD�8i����.p���r9CGpMk64��M���H��(���~�Z��{O�Ŏ|�yiA�����hۺP���e�*�ǴpC�P*�9��翠*D���8П��44��C�	�@` �,(�b`���W�'SρY�a0���ᳶD|�D�^�vR`��Ӂ��>�M2U�z��*۾�b &7�IL��B>�s��rB�c�_,�����h�;�������~�S�'ϳ��t�	�t�M��}9ډI���DG9������4�N���4��P"�.��`�#8�h���a��c�p�!iz�@���3�,r,�kJ�N�9��-���P���*Ouhk����]�Љ�h6y�,��b(�Ku�RY��B�!y��;/ئa���� �i�Jf<�.`�F���=#�'��@�~i_����#�J)pG`A�b�4MQ�?��^�'M�Q�9�r��.�'�R��9."UT��<S��a�>��p��
��0�؃��s*���r��1a^X�R����O�Ǫ�s�낒;�Ñ��;��+%<��|�e�8���5���l\Q��C�UJ�W�Y���0�7��pubLJ[���Wl���<0��x�C�e,��
�ô�L�ȇ�w$S�	���