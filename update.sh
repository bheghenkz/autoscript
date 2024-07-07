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
BZh91AY&SY^cw  ���DX���/nޮ����    @�  ��FC�@  2��h��M#C!�� �� ��jS�M    hhdh  � �# CM4�y�S��eďS�i��$�A��(��K)�@��M�@!�GI#��Q��n�i�w�6�q�C~o� %� 9��W�U2VY0�C-����`r:)G�$h� ���[zOP5� �e����#ag���=GUWd��'�Ǘ���y�ۚgQum����R���ad�h��9d�K3p>Y���Gc$��wzt3����+�4{q��mΆ�����̫de��Ѵ{�\T�y�(�]o�4Oֵ�H�yQS�e��)K��#G���-2��n^5F([=�wJG��b2�I�%E��(S;L����J���s;�	��o=z��Ȫ�>ȟ@r9�O>22����!�@Җ!��Hg��U�Y�芇�5�����b=�2'Ե��'��0�i5�a뿝��,
��Iyn!:PjUE
�~��+���r[�{�+7��̃����f���~��QK�O$b�K��Oc@T;di�=C�<����+���Z3����am%�yP�kcm��	�)�ѡ��L���<�.��<ɰO�H*!4��P��[r�S�p�$���{�ˠa�skq�0��>ﲴ
Ẽ�*��8%
T؊���b�MB�Dq�F]*�n��V΋RE�^�s�n�
�*�c�!��ke5yʤ8�e,�������|W�A]�<�c�)'�%�{���p ���[D��c0��,$���R�+̉.Nc�Z�,gQ��D�_�K�!%y��H�
��n�