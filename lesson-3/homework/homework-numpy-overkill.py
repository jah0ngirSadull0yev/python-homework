import numpy as np
import random
from collections import defaultdict

def array_automator(id, l1 = None, l2 = None, a = None, b = None, idx1 = None, idx2 = None):

    arr1 = np.array(l1) if l1 is not None else np.array([])
    arr2 = np.array(l2) if l2 is not None else np.array([])
    is_empty = arr1.size == 0

    match id:
        case 1:
            return int(np.sum(arr1 == a))
        case 2:
            return int(np.sum(arr1)) if not is_empty else 0
        case 3:
            return int(np.max(arr1)) if not is_empty else None
        case 4:
            return int(np.min(arr1)) if not is_empty else None
        case 5:
            return bool(np.any(arr1 == a))
        case 6:
            return arr1[0].item() if not is_empty else None
        case 7:
            return arr1[-1].item() if not is_empty else None
        case 8:
            return arr1[:3].tolist() if arr1.size >= 3 else arr1.tolist()
        case 9:
            return arr1[::-1].tolist()
        case 10:
            return np.sort(arr1).tolist()
        case 11:
            _, indices = np.unique(arr1, return_index=True)
            return arr1[np.sort(indices)].tolist()
        case 12:
            return np.insert(arr1, idx1, a).tolist()
        case 13:
            matches = np.flatnonzero(arr1 == a)
            return int(matches[0]) if matches.size > 0 else -1
        case 14:
            return is_empty
        case 15:
            return int(np.sum((arr1 & 1) == 0))
        case 16:
            return int(np.sum(arr1 & 1))
        case 17:
            return [*l1, *l2]
        case 18:
            n, m = arr1.size, arr2.size
            t = np.arange(n - m + 1)[:, None] + np.arange(m)
            r = arr1[t]
            return np.any(np.all(r == arr2, axis=1))
        case 19:
            m = (arr1 == a)
            if np.any(m):
                i = np.argmax(m)
                arr1[i] = b
            return arr1.tolist()
        case 20:
            m = np.max(arr1)
            t = arr1[arr1 != m]
            if t.size == 0:
                return None
            return arr1[np.argmax(t)].item()
        case 21:
            m = np.min(arr1)
            t = arr1[arr1 != m]
            if t.size == 0:
                return None
            return arr1[np.argmin(t)].item()
        case 22:
            return arr1[~(arr1 & 1).astype(bool)].tolist()
        case 23:
            return arr1[(arr1 & 1).astype(bool)].tolist()
        case 24:
            return arr1.size
        case 25:
            return arr1.tolist()
        case 26:
            ln = arr1.size
            if ln & 1:
                return arr1[ln//2].item()
            elif ln == 0:
                return None
            else:
                return [arr1[ln//2 - 1].item(), arr1[ln//2].item()]
        case 27:
            return np.max(arr1[idx1:idx2]).item()
        case 28:
            return np.min(arr1[idx1:idx2]).item()
        case 29:
            return np.delete(arr1, idx1).tolist() if idx1 < arr1.size else arr1.tolist()
        case 30:
            if arr1.size < 2: 
                return True
            ar1 = arr1[1:]
            ar2 = arr1[:-1]
            return np.all(ar2 <= ar1)
        case 31:
            return np.repeat(arr1, a).tolist()
        case 32:
            return np.sort(np.concatenate((arr1, arr2))).tolist()
        case 33:
            i = np.arange(arr1.size)
            return i[arr1 == a].tolist()
        case 34:
            if idx1 is None:
                idx1 = 1
            return np.roll(arr1, idx1).tolist()
        case 35:
            return np.arange(a, b + 1).tolist()
        case 36:
            return np.sum(arr1[arr1 > 0]).item()
        case 37:
            return np.sum(arr1[arr1 < 0]).item()
        case 38:
            arr = arr1[::-1]
            return np.all(arr1 == arr)
        case 39:
            i = np.cumsum(arr2)[:-1]
            ans = np.split(arr1, i)
            return [x.tolist() for x in ans]
        case 40:
            _, i = np.unique(arr1, return_index=True)
            return arr1[np.sort(i)].tolist()
        case _:
            return None


def tuple_automator(id, t1 = None, t2 = None, a = None, b = None, idx1 = None, idx2 = None):

    arr1 = np.array(t1) if t1 is not None else np.array(())
    if id != 20:
        arr2 = np.array(t2) if t2 is not None else np.array(())
    is_empty = arr1.size == 0

    match id:
        case 1:
            return np.sum(arr1 == a).item() if not is_empty else 0
        case 2:
            return np.max(arr1).item() if not is_empty else None
        case 3:
            return np.min(arr1).item() if not is_empty else None
        case 4:
            return np.any(arr1 == a).item()
        case 5:
            return arr1[0].item() if not is_empty else None
        case 6:
            return arr1[-1].item() if not is_empty else None
        case 7:
            return arr1.size
        case 8:
            return tuple(arr1[:3].tolist())
        case 9:
            return tuple(np.concatenate((arr1, arr2)).tolist())
        case 10:
            return is_empty
        case 11:
            return np.flatnonzero(arr1 == a).tolist()
        case 12:
            mx = np.max(arr1) if not is_empty else None
            matches = arr1[arr1 != mx] if mx is not None else np.array([])
            return max(matches).item() if matches.size > 0 else None
        case 13:
            mn = np.min(arr1) if not is_empty else None
            matches = arr1[arr1 != mn] if mn is not None else np.array([])
            return min(matches).item() if matches.size > 0 else None
        case 14:
            return (a,)
        case 15:
            return tuple(t1)
        case 16:
            return np.all(np.diff(arr1) >= 0)
        case 17:
            return np.max(arr1[idx1:idx2]).item() if arr1[idx1:idx2].size != 0 else None
        case 18:
            return np.min(arr1[idx1:idx2]).item() if arr1[idx1:idx2].size != 0 else None
        case 19:
            idx = np.flatnonzero(arr1 == a)
            return tuple(np.delete(arr1, idx[0]).tolist()) if idx.size > 0 else t1
        case 20:
            sizes = [len(i) for i in t2]
            si = np.cumsum(sizes)[:-1]
            arr2 = np.concatenate(t2)
            res = arr1[arr2]
            ans = np.split(res, si)
            return tuple(tuple(i.tolist()) for i in ans)
        case 21:
            return tuple(np.repeat(arr1, a).tolist())
        case 22:
            return tuple(np.arange(a, b).tolist())
        case 23:
            return tuple(arr1[::-1].tolist())
        case 24:
            return np.all(arr1 == arr1[::-1])
        case 25:
            _, index = np.unique(arr1, return_index=True)
            index.sort()
            return tuple(arr1[index].tolist())
        case _:
            return None


def set_automator(id, s1 = None, s2 = None, a = None, b = None, n = None):

    match id:
        case 1:
            return s1 | s2
        case 2:
            return s1 & s2
        case 3:
            return s1 - s2
        case 4:
            return s1 <= s2 or s2 <= s1
        case 5:
            return a in s1
        case 6:
            return len(s1)
        case 7:
            return set(s1)
        case 8:
            s1.discard(a)
            return s1
        case 9:
            s1.clear()
            return s1
        case 10:
            return len(s1) == 0
        case 11:
            return s1 ^ s2
        case 12:
            s1.add(a)
            return s1
        case 13:
            return s1.pop()
        case 14:
            return max(s1)
        case 15:
            return min(s1)
        case 16:
            return {i for i in s1 if i % 2 == 0}
        case 17:
            return {i for i in s1 if i % 2 == 1}
        case 18:
            return {i for i in range(a, b)}
        case 19:
            return set(s1) | set(s2)
        case 20:
            return len(s1 & s2) == 0
        case 21:
            s1 = list(set(s1))
            return s1
        case 22:
            return len(set(s1))
        case 23:
            res = set()
            while len(res) < n:
                res.add(random.randint(a, b))
            return res
        case _:
            return None


def dict_automator(id, d1 = None, d2 = None, k1 = None, v1 = None, f = None): # f is lambda

    match id:
        case 1:
            return d1.get(k1) if k1 in d1 else None
        case 2:
            return k1 in d1
        case 3:
            return len(d1.keys())
        case 4:
            return list(d1.keys())
        case 5:
            return list(d1.values())
        case 6:
            return {**d1, **d2}
        case 7:
            if k1 in d1:
                d1.pop(k1)
            return d1
        case 8:
            return {}
        case 9:
            return len(d1) == 0
        case 10:
            return (k1, d1.get(k1)) if k1 in d1 else ()
        case 11:
            if k1 in d1:
                d1[k1] = v1
            return d1
        case 12:
            return sum(v1 == v for v in d1.values())
        case 13:
            return {v: k for k, v in d1.items()}
        case 14:
            return [i for i, v in d1.items() if v == v1]
        case 15:
            return dict(zip(d1, d2))
        case 16:
            return any(isinstance(v, dict) for v in d1.values())
        case 17:
            for v in d1.values():
                if isinstance(v, dict) and k1 in v:
                    return v[k1]
            return None
        case 18:
            d = defaultdict(lambda: v1)
            if d1:
                d.update(d1)
            return d
        case 19:
            return len(set(d1.values()))
        case 20:
            return {i: d1[i] for i in sorted(d1)}
        case 21:
            return {k: v for k, v in sorted(d1.items(), key=lambda x: x[1])}
        case 22:
            return {k: v for k, v in d1.items() if f(v)}
        case 23:
            return any(k in d2 for k in d1)
        case 24:
            return dict(d1)
        case 25:
            x = list(d1.items())
            return x[0] if len(x) > 0 else None
        case _:
            return None



