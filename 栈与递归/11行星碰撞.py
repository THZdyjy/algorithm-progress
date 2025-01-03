class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        st = []
        for aster in asteroids:
            alive = True
            # 行星为正，append; 刚开始为负，append; 为负，且前一个也为负，append;
            # 剩下的情况，就是行星为负，其前一个为正，则二者要碰撞
            while alive and aster < 0 and st and st[-1] > 0:
                alive = st[-1] < -aster
                # 如果前一颗小于等于当前的，pop
                if st[-1] <= -aster:
                    st.pop()
            if alive:
                st.append(aster)
        return st

