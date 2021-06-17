import React from "react";
import {Heading, Flex, Divider, Center, IconButton} from "@chakra-ui/react";

const Header = () => {
    return (

        <Flex
            as="nav"
            align="center"
            pos="center"
            justify="space-between"
            wrap="wrap"
            padding="1rem"
            bg="white"
        >
            <Flex align="center" mr={5}>
                <Heading as="h2" size="xl" align="center">Notes!</Heading>
            </Flex>
        </Flex>

    );
};

export default Header;