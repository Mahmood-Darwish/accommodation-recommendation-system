import unittest
import server
import pickle as pk

clusters = pk.load(open("cluster_centers.pkl", 'rb'))


class TestStringMethods(unittest.TestCase):

    def test_calcDisToRoom(self):
        testcase1 = [[-1, 1, 1, 0], 0, 0]
        room1 = [0, 0, [1, 1, 1, 1], [1, 1, 1, 0], [], [], []]
        self.assertEqual(server.calcDisToRoom(
            testcase1[0], testcase1[1], testcase1[2], room1), 2.5)
        testcase2 = [[0, 0, 0, 0], 1, 2]
        room2 = [0, 0, [1, 1, 1, 1], [1, 1, 1, 0], [], [], []]
        self.assertEqual(server.calcDisToRoom(
            testcase2[0], testcase2[1], testcase2[2], room2), 7)
        testcase3 = [[0, 0, 0, 0], 0, 2]
        room3 = [0, 0, [1, 1, 1, 1], [1, 1, 1, 0], [], [], []]
        self.assertEqual(server.calcDisToRoom(
            testcase3[0], testcase3[1], testcase3[2], room3), 1.75)

    def test_getClusterCenter(self):
        testcase1 = [1, 1, 1, 1]
        self.assertAlmostEqual(server.getClusterCenter(testcase1)[0], -0.02742723)
        self.assertAlmostEqual(server.getClusterCenter(testcase1)[1], 0.06202015)
        self.assertAlmostEqual(server.getClusterCenter(testcase1)[2], 0.91437895)
        self.assertAlmostEqual(server.getClusterCenter(testcase1)[3], 1.98951465)
        self.assertEqual(len(server.getClusterCenter(testcase1)), 4)
        testcase2 = [-1, -1, -1, -1]
        self.assertAlmostEqual(server.getClusterCenter(testcase2)[0], 0.65816276)
        self.assertAlmostEqual(server.getClusterCenter(testcase2)[1], -1.24345945)
        self.assertAlmostEqual(server.getClusterCenter(testcase2)[2], -2.13923283)
        self.assertAlmostEqual(server.getClusterCenter(testcase2)[3], -0.31232172)
        self.assertEqual(len(server.getClusterCenter(testcase2)), 4)
        testcase3 = [-0.5, -1, 1.2, 0]
        self.assertAlmostEqual(server.getClusterCenter(testcase3)[0], -1.4559407)
        self.assertAlmostEqual(server.getClusterCenter(testcase3)[1], -2.87944546)
        self.assertAlmostEqual(server.getClusterCenter(testcase3)[2], 1.13639728)
        self.assertAlmostEqual(server.getClusterCenter(testcase3)[3], -0.17672055)
        self.assertEqual(len(server.getClusterCenter(testcase3)), 4)


if __name__ == '__main__':
    unittest.main()
